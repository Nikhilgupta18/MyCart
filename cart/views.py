from django.shortcuts import render, redirect, reverse
from .models import Cart
from product.models import Product
from django.contrib.auth.decorators import login_required


def cart(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    context = {
        'cart': cart_obj,

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
    print(request.POST)
    product_id = request.POST.get('product_id')
    if product_id is not None:
        product = Product.objects.get(id=product_id)
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product in cart_obj.products.all():
            cart_obj.products.remove(product)
        else:
            cart_obj.products.add(product)
    return redirect(reverse('cart'))

