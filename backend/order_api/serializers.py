from rest_framework import serializers
from .models import Cart, CartItem, Order, OrderItem, Coupon
from product_api.serializers import ProductSerializer

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)
    cost = serializers.ReadOnlyField(source='get_cost')

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_id', 'quantity', 'cost']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.ReadOnlyField(source='get_total_price')

    class Meta:
        model = Cart
        fields = ['id', 'items', 'total_price']

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    cost = serializers.ReadOnlyField(source='get_cost')

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'price', 'quantity', 'cost']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'total_amount', 'shipping_address', 'coupon', 'items', 'created_at']
        read_only_fields = ['id', 'user', 'status', 'total_amount', 'created_at']
