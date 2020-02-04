from django.shortcuts import render
from product import models
from math import ceil


# Create your views here.


def Clothing_Display(request):
    products = models.Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'clothing.html', context)


def Electronics_Display(request):
    products = models.Product.objects.all()
    context = {
        'products': products,

    }
    return render(request, 'electronics.html', context)


def Education_Display(request):
    products = models.Product.objects.all()
    context = {
        'products': products,

    }
    return render(request, 'education.html', context)


def Sports_Display(request):
    products = models.Product.objects.all()
    context = {
        'products': products,

    }
    return render(request, 'sports.html', context)
