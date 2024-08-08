from django.contrib import admin

from apps.orders.models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_amount']
    list_display_links = ['user']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']
    list_display_links = ['order', 'product']


