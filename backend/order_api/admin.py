from django.contrib import admin
from .models import Cart, CartItem, Order, OrderItem, Coupon

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'item_count', 'total_price')
    inlines = [CartItemInline]
    
    def item_count(self, obj):
        return obj.items.count()
    
    def total_price(self, obj):
        return obj.get_total_price()

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('price', 'quantity', 'get_cost')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'total_amount', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('shipping_address', 'user__username')
    list_editable = ('status',)
    inlines = [OrderItemInline]
    readonly_fields = ('total_amount', 'created_at', 'updated_at')

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'active', 'expiry_date')
    list_filter = ('active', 'expiry_date')
    search_fields = ('code',)
