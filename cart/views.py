from django.shortcuts import render, redirect, reverse
from .models import Cart
from product.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from orders.models import Order

def cart(request):
    if request.user.is_authenticated:
        cart_obj = Cart.objects.get(user=request.user)
    else:
        cart_obj = Cart.objects.get(id=request.session.get('cart_id'))
    # if request.user.is_authenticated and cart_obj.user is None:
    #     if Cart.objects.filter(user=request.user).exists:
    #         cart_obj = Cart.objects.get(user=request.user)
    #     else:
    #         cart_obj.user = request.user
    #         cart_obj.save()

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        if product_id is not None:
            product = Product.objects.get(id=product_id)
            if product in cart_obj.products.all():
                cart_obj.products.remove(product)
                messages.error(request, '%s Removed from cart' % product)

    n = len(cart_obj.products.all())
    if cart_obj.total and cart_obj.subtotal == cart_obj.total:
        del_fee = 0
    else:
        del_fee = 25

    context = {
        'cart': cart_obj,
        'items': n,
        'del_fee': del_fee,

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
            messages.error(request, '%s Removed from cart' % product)
        else:
            cart_obj.products.add(product)
            messages.success(request, '%s Added to cart' % product)

    return redirect(reverse('cart'))


def checkout(request):
    if request.user.is_authenticated:
        cart_obj = Cart.objects.get(user=request.user)
    else:
        cart_obj = Cart.objects.get(id=request.session.get('cart_id'))

    order_obj = None
    if cart_obj.products.count() == 0:
        return redirect(reverse('cart'))
    else:
        order_obj, new_order_obj = Order.objects.get_or_create(cart=cart_obj)
    context = {
        'order': order_obj
    }
    return render(request, 'order.html', context)

