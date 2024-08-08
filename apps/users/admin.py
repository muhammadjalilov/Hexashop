from django.contrib import admin
from apps.users.models import User, Services


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'is_staff', 'email', 'phone', 'role']
    list_display_links = ['username']


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['heading', 'description'[:50]]
    list_display_links = ['heading']
