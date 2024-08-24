from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from apps.cart.cart import Cart
from apps.orders.forms import OrderCreateForm
from apps.orders.models import OrderItem, Order
from apps.users.models import ClientDetails, User


@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            client_details = ClientDetails.objects.create(
                user=request.user,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                region=form.cleaned_data['region'],
                city=form.cleaned_data['city'],
                street=form.cleaned_data['street'],
                flat_number=form.cleaned_data['flat_number']

            )
            form.instance.client = client_details
            order = form.save()
            for item in cart:
                order_item = OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            return render(request,
                              'orders/created-order.html',
                              {'order_item': order_item})
        else:
            return HttpResponse('invalid')
    else:
        initial_data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }
        form = OrderCreateForm(initial=initial_data)
    return render(request,
                  'orders/create-order.html',
                  {'cart': cart, 'form': form})


class ShowUserOrdersView(LoginRequiredMixin, View):
    template_name = 'orders/user_orders.html'

    def get(self, request):
        orders = (
            Order.objects
            .filter(client__user=self.request.user)
            .select_related('client__user','client')
            .prefetch_related(
                Prefetch('items', queryset=OrderItem.objects.select_related('product'))
            )
            .order_by('-created_at')
        )
        context = {'orders': orders}
        return render(request, template_name=self.template_name, context=context)
