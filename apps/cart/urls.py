from django.urls import path

from apps.cart.views import cart_detail, cart_remove, cart_add

app_name = 'cart'
urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
    path('add/<int:product_id>/', cart_add, name='cart_add'),
]
