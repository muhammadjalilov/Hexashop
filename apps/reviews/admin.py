from django.contrib import admin

from apps.reviews.models import Review


@admin.register(Review)
class ReviewsConfigAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'comment']
    list_display_links = ['product', 'rating']
    ordering = ('-rating',)
