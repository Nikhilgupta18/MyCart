from django.shortcuts import render
from product import models
from django.views.generic import (
    TemplateView,
    DetailView,
    ListView
)
from math import ceil


# Create your views here.


def ClothingDisplay(request):
    product = models.Product.objects.filter(P_category='C')
    context = {
        'product': product,

    }
    return render(request, 'product_view.html', context)


def ElectronicsDisplay(request):
    product = models.Product.objects.filter(P_category='E')
    context = {
        'product': product,

    }
    return render(request, 'product_view.html', context)


def EducationDisplay(request):
    product = models.Product.objects.filter(P_category='Ed')
    context = {
        'product': product,

    }
    return render(request, 'product_view.html', context)


def SportsDisplay(request):
    product = models.Product.objects.filter(P_category='S')
    context = {
        'product': product,

    }
    return render(request, 'product_view.html', context)



class ProductView(DetailView):
    model = models.Product
    template_name='product.html'
