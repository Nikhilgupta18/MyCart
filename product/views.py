from django.shortcuts import render
from product import models
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView
)
from math import ceil


# Create your views here.






class ProductView(DetailView):
    model = models.Product
    template_name='product.html'


def prod_cat(request, category):
    cat = models.Product.objects.filter(P_category=category)
    print(cat)
    context = {
        'product': cat,
    }

    return render(request, 'product_view.html', context)
