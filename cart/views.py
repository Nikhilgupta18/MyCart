from django.shortcuts import render, redirect, reverse
from .models import Cart
from product.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def cart(request):
    # cart = Cart.objects.filter(User=request.user)
    if request.user.is_authenticated:
        cart_obj = Cart.objects.get(user=request.user)

        # try:
        #     cart_obj = Cart.objects.get(user=request.user)
        # except:
        #     cart_obj = Cart.objects.create(user=request.user)
    else:
        cart_obj = Cart.objects.get(id=request.session.get('cart_id'))
    # cart_obj, new_obj = Cart.objects.new_or_get(request)
    n = len(cart_obj.products.all())
    context = {
        'cart': cart_obj,
        'items': n,

    }
    return render(request, 'cart.html', context)
    # print(request.session.session_key)
    # request.session["first_name"] = "Nikhil"
    # request.session['user'] = request.user.username
    # print(request.session.get('user'))
    # request.session.set_expiry(300)  this allows us to end the session in milliseconds, here = 5 mins

# @login_required()
# def test(request):
#     print(request.user)
#     if Cart.objects.filter(user=request.user).exists():
#         cart_obj = Cart.objects.filter(user=request.user)
#         print('exists',cart_obj)
#     return render(request, 'cart.html', {'cart': cart_obj})

# @login_required()


def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        product = Product.objects.get(id=product_id)
        # cart_obj, new_obj = Cart.objects.new_or_get(request)
        if request.user.is_authenticated:
            cart_obj = Cart.objects.get(user=request.user)
        else:
            cart_obj = Cart.objects.get(id=request.session.get('cart_id'))
        if product in cart_obj.products.all():
            cart_obj.products.remove(product)
            messages.warning(request, 'Removed from cart')
        else:
            cart_obj.products.add(product)
            messages.success(request, 'Added to cart')

    return redirect(reverse('cart'))

