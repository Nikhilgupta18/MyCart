from django.shortcuts import render
from product import models
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView
)
from math import ceil
from .filters import ProductFilter
from cart.models import Cart


class ProductView(DetailView):
    model = models.Product

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            # try:
            cart_obj = Cart.objects.get(user=self.request.user)
            # except:
            #     cart_obj = Cart.objects.create(user=self.request.user)
        else:
            cart_obj = Cart.objects.get(id=self.request.session.get('cart_id'))
        n = len(cart_obj.products.all())
        context['cart'] = cart_obj
        context['items'] = n
        return context

    template_name = 'product.html'


def prod_cat(request, category):
    cat = models.Product.objects.filter(P_category=category)
    if request.user.is_authenticated:
        # try:
        cart_obj = Cart.objects.get(user=request.user)
        # except:
        #     cart_obj = Cart.objects.create(user=request.user)
    else:
        cart_obj = Cart.objects.get(id=request.session.get('cart_id'))

    n = len(cart_obj.products.all())
    context = {
        'product': cat,
        'cart': cart_obj,
        'items': n,

    }

    return render(request, 'product_view.html', context)


