from django.shortcuts import render
from .models import Cart


def cart(request):
    cart_obj = Cart.objects.new_or_get(request)
    context = {
        'cart': cart_obj
    }
    return render(request, 'cart.html', context)
    # print(request.session.session_key)
    # request.session["first_name"] = "Nikhil"
    # request.session['user'] = request.user.username
    # print(request.session.get('user'))
    # request.session.set_expiry(300)  this allows us to end the session in milliseconds, here = 5 mins
