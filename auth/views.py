from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm
from django.contrib.auth.views import (
    LoginView,
    LogoutView
)
from twilio.rest import Client

account_sid = "AC2f8b02a70dd42f2e5510371fadf68081"
auth_token = "d5a84293168739e0e89cb8352aa79ac5"

client = Client(account_sid, auth_token)


def send_sms(request):
    sms = client.messages.create(
        from_="+18645318454",
        body="Welcome to My Cart! Grab the Exciting offers and fill your cart. Happy shopping!!",
        to="+919354324266"
    )
    print(sms.sid)
    return render(request, 'activate.html')


# Create your views here.
class Login(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True


class Logout(LogoutView):
    next_page = '/'


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/auth/activate/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
