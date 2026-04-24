from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, Review, Wishlist

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'vendor', 'category', 'price', 'stock', 'is_active', 'image_tag')
    list_filter = ('is_active', 'category', 'vendor', 'created_at')
    search_fields = ('name', 'description')
    list_editable = ('price', 'stock', 'is_active')
    autocomplete_fields = ('vendor', 'category')
    
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 45px; height:45px; border-radius: 50%;" />'.format(obj.image.url))
        return "-"
    image_tag.short_description = 'Preview'

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('comment',)

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'product_count')
    
    def product_count(self, obj):
        return obj.products.count()
    product_count.short_description = 'Products in Wishlist'