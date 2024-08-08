from django.contrib.auth import get_user_model
from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import TemplateView

from apps.product.models import Category
from apps.users.models import Services


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['men'] = Category.objects.get(name='Men').products.all().order_by('-created_at')[:5]
        context['women'] = Category.objects.get(name='Women').products.all().order_by('-created_at')[:5]
        context['kids'] = Category.objects.get(name='Kids').products.all().order_by('-created_at')[:5]
        socials = [
            {'name': 'Fashion', 'url': f'images/instagram-01.jpg'},
            {'name': 'New', 'url': f'images/instagram-02.jpg'},
            {'name': 'Brand', 'url': f'images/instagram-03.jpg'},
            {'name': 'Makeup', 'url': f'images/instagram-04.jpg'},
            {'name': 'Leather', 'url': f'images/instagram-05.jpg'},
            {'name': 'Bag', 'url': f'images/instagram-06.jpg'}
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
