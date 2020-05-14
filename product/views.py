from django.shortcuts import render
from product import models
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView
)
from math import ceil
from cart.models import Cart


class ProductView(DetailView):
    model = models.Product

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    template_name = 'product.html'


def prod_cat(request, category):
    cat = models.Product.objects.filter(P_category=category)
    print(cat)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    context = {
        'product': cat,
        'cart': cart_obj,
    }

    return render(request, 'product_view.html', context)
