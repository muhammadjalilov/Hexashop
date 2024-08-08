from django.contrib import admin

from apps.cart.models import CartItem, Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_display_links = ['user']


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'quantity']
    list_display_links = ['quantity']
