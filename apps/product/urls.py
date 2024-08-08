from django.urls import path

from apps.product.views import AllProductsView, SingleProductView

app_name = 'product'
urlpatterns = [
    path('', AllProductsView.as_view(), name='products'),
    path('product/<slug:slug>/', SingleProductView.as_view(), name='product'),
]
