from django.shortcuts import render
from product import models
from math import ceil

# Create your views here.


def index(request):
    print(request.session.get("first_name", "Unknown"))
    product = models.Product.objects.all()
    n = len(product)
    slides = n // 4 + ceil((n / 4) - (n // 4))
    context = {
        'product': product,
        'slides': slides,
        'range': range(1,slides),
    }
    return render(request, 'main/index2.html', context)

