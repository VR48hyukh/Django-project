from django.contrib.auth import admin

from .models import Profile, Product, Cart, Category

@admin.register(Product)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('name', 'price', 'is_available', 'text', 'category', )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name', )

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','image','total_price', )

@admin.register(Cart)
class CartItemAdmin(admin.ModelAdmin):
    list_display=('user', 'count', 'product_name', )
