from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from apps.cart.cart import Cart
from apps.cart.forms import CartAddProductForm
from apps.product.models import Product


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            override_quantity=cd['override']
        )

    # Get the referrer URL (the previous page)
    previous_url = request.META.get('HTTP_REFERER')

    # If there is a previous URL and it's not the cart detail page, redirect back to it
    if 'products/product' in previous_url:
        return redirect('cart:cart_detail')

    # Otherwise, redirect to the cart detail page
    return HttpResponseRedirect(previous_url)


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    # Get the referrer URL (the previous page)
    previous_url = request.META.get('HTTP_REFERER')

    # If there is a previous URL and it's not the cart detail page, redirect back to it
    if 'cart' in previous_url:
        return redirect('cart:cart_detail')

    # Otherwise, redirect to the cart detail page
    return HttpResponseRedirect(previous_url)


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'], 'override': True}
        )
    return render(request, 'cart/detail.html', {'cart': cart})
