from django.shortcuts import render, redirect, reverse
from product.models import Product
from product.filters import ProductFilter
from math import ceil
from cart.models import Cart
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
import csv
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm, AdminPasswordChangeForm


# Create your views here.


def index(request):
    # print(request.session.get("first_name", "Unknown"))
    # product = Product.objects.filter(P_offer='N')
    product = Product.objects.all()
    if request.user.is_authenticated:
        try:
            cart_obj = Cart.objects.get(user=request.user)
        except:
            cart_obj = Cart.objects.create(user=request.user)
    else:
        try:
            cart_obj = Cart.objects.get(id=request.session.get('cart_id'))
        except:
            cart_obj = Cart.objects.create(user=None)
            request.session['cart_id'] = cart_obj.id
    cart_items = len(cart_obj.products.all())

    n = len(product)
    slides = n // 4 + ceil((n / 4) - (n // 4))
    context = {
        'product': product,
        'slides': slides,
        'range': range(1, slides),
        'items': cart_items,
    }
    return render(request, 'main/index2.html', context)


def search_results(request):
    query = request.GET['query']
    if len(query) > 100:
        products = Product.objects.none()
    else:
        # productsName = Product.objects.filter(P_name__icontains=query)
        # productsDesc = Product.objects.filter(P_desc__icontains=query)
        # products = productsName.union(productsDesc)
        products = Product.objects.filter(Q(P_name__icontains=query) | Q(P_desc__icontains=query))
    filter = ProductFilter(request.GET, queryset=products)
    if filter.qs.count() == 0:
        messages.warning(request, 'No results found!')
    print(query)
    context = {
        'product': products,
        'query': query,
        'filter': filter
    }
    return render(request, 'search-results.html', context)


def download_data(request, query=None):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Products.csv"'

    writer = csv.writer(response)
    writer.writerow(['Product', 'MRP', 'Price'])
    products = Product.objects.filter(Q(P_name__icontains=query) | Q(P_desc__icontains=query)).values_list(
        'P_name', 'P_price', 'disc_price'
    )

    for user in products:
        writer.writerow(user)

    return response


@login_required
def change_password(request):
    username = request.GET.get('username')
    user_obj = User.objects.get(username=username)
    form = AdminPasswordChangeForm(user=user_obj)
    if request.method == 'POST':
        form = AdminPasswordChangeForm(data=request.POST, user=user_obj)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('index'))
    return render(request, 'change-password.html', {'form': form, 'user': user_obj})


@login_required
def user_search_reset_password(request):
    return render(request, 'user-password-reset.html')
