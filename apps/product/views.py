from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView

from apps.cart.forms import CartAddProductForm
from apps.product.models import Product, Category


class AllProductsView(ListView):
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 9

    def get_queryset(self):
        return Product.objects.all()


class SingleProductView(DetailView):
    model = Product
    template_name = 'single-product.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context


def product_detail(request, slug):
    product = get_object_or_404(
        Product, slug=slug, available=True
    )
    cart_product_form = CartAddProductForm()
    return render(
        request,
        'single-product.html',
        {'product_cart': product, 'cart_product_form': cart_product_form}
    )
