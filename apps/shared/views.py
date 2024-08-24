from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.db.models import Prefetch
from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import TemplateView

from apps.cart.forms import CartAddProductForm
from apps.product.models import Category, Product
from apps.users.models import Services


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        categories = Category.objects.all().prefetch_related(
            Prefetch('products', queryset=Product.objects.all())
        )

        context['categories'] = categories

        context['men'] = next((category.products.all()[:5] for category in categories if category.name == 'Men'), [])
        context['women'] = next((category.products.all()[:5] for category in categories if category.name == 'Women'),
                                [])
        context['kids'] = next((category.products.all()[:5] for category in categories if category.name == 'Kids'), [])

        context['form'] = CartAddProductForm()

        socials = [
            {'name': 'Fashion', 'url': 'images/instagram-01.jpg'},
            {'name': 'New', 'url': 'images/instagram-02.jpg'},
            {'name': 'Brand', 'url': 'images/instagram-03.jpg'},
            {'name': 'Makeup', 'url': 'images/instagram-04.jpg'},
            {'name': 'Leather', 'url': 'images/instagram-05.jpg'},
            {'name': 'Bag', 'url': 'images/instagram-06.jpg'}
        ]
        context['socials'] = socials

        return context


class AboutUsView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team'] = get_user_model().objects.exclude(role='Customer').all()
        context['services'] = Services.objects.all().order_by('-created_at')[:3]
        return context
