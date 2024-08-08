from django.contrib import admin

from apps.product.models import Product, Category, Discount


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'slug', 'created_at', 'available']
    list_display_links = ['name']
    list_filter = ['name', 'price']
    ordering = ['-created_at']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'short_description', 'image']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['product', 'discount_percentage', 'start_date', 'end_date']
    list_display_links = ['discount_percentage']
