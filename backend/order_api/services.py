from django.db import transaction
from .models import Order, OrderItem, Cart, CartItem, Coupon
from product_api.models import Product
from decimal import Decimal
from django.conf import settings

def process_order(user, shipping_address, coupon_code=None):
    cart = Cart.objects.filter(user=user).first()
    if not cart or not cart.items.exists():
        raise Exception("Cart is empty")

    with transaction.atomic():
        total_amount = cart.get_total_price()
        coupon = None
        if coupon_code:
            coupon = Coupon.objects.filter(code=coupon_code, active=True).first()
            if coupon:
                discount_amount = total_amount * (coupon.discount / Decimal(100))
                total_amount -= discount_amount

        # Create Order
        order = Order.objects.create(
            user=user,
            shipping_address=shipping_address,
            total_amount=total_amount,
            coupon=coupon
        )

        # Create Order Items and update stock
        for item in cart.items.all():
            if item.product.stock < item.quantity:
                raise Exception(f"Not enough stock for {item.product.name}")
            
            OrderItem.objects.create(
                order=order,
                product=item.product,
                price=item.product.price,
                quantity=item.quantity
            )
            
            # Update stock
            item.product.stock -= item.quantity
            item.product.save()

        # Clear Cart
        cart.items.all().delete()

        return order

def simulate_payment(order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        raise Exception("Order not found")
    # In a real app, this would involve Stripe/PayPal API
    order.status = 'PAID'
    order.save()
    return True
