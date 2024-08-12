from django.urls import path

from apps.orders.views import order_create, ShowUserOrdersView

app_name = 'orders'

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('show-orders/', ShowUserOrdersView.as_view(), name='show_orders'),
]
