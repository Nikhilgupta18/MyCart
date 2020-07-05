from django.shortcuts import render
from product.models import Product
from math import ceil
from cart.models import Cart
from django.contrib import messages


# Create your views here.


def index(request):
    # print(request.session.get("first_name", "Unknown"))
    # product = Product.objects.filter(P_offer='N')
    product = Product.objects.all()
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
    cart_items = len(cart_obj.products.all())

    n = len(product)
    slides = n // 4 + ceil((n / 4) - (n // 4))
    context = {
        'product': product,
        'slides': slides,
        'range': range(1, slides),
        'items': cart_items,
    }
    return render(request, 'main/index2.html', context)


def search_results(request):
    query = request.GET['query']
    if len(query) > 10:
        products = Product.objects.none()
    else:
        productsName = Product.objects.filter(P_name__icontains=query)
        productsDesc = Product.objects.filter(P_desc__icontains=query)
        products = productsName.union(productsDesc)
    if products.count() == 0:
        messages.warning(request, 'No results found!')
    context = {
        'product': products,
        'query': query
    }
    return render(request, 'search-results.html', context)
