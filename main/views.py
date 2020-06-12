from django.shortcuts import render
from product import models
from math import ceil
from cart.models import Cart
# Create your views here.


def index(request):
    # print(request.session.get("first_name", "Unknown"))
    product = models.Product.objects.all()
    if request.user.is_authenticated:
        try:
            cart_obj = Cart.objects.get(user=request.user)
        except:
            cart_obj = Cart.objects.create(user=request.user)
    else:
        try:
            cart_obj = Cart.objects.get(id=request.session.get('cart_id'))
        except:
            cart_obj = Cart.objects.create(user=None)
            request.session['cart_id'] = cart_obj.id
    print(request.session.session_key)
    cart_items = len(cart_obj.products.all())
    n = len(product)
    slides = n // 4 + ceil((n / 4) - (n // 4))
    context = {
        'product': product,
        'slides': slides,
        'range': range(1,slides),
        'items': cart_items,
    }
    return render(request, 'main/index2.html', context)

