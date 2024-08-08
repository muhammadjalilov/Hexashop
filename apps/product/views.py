from django.views.generic import ListView, DetailView

from apps.product.models import Product, Category


class AllProductsView(ListView):
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 9

    def get_queryset(self):
        return Product.objects.all().order_by('-created_at')


class SingleProductView(DetailView):
    model = Product
    template_name = 'single-product.html'
    context_object_name = 'product'
