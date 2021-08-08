from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserSignUpForm, UserLoginForm

# Create your views here.

def signup_view(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core:index')
    else:
        form = UserSignUpForm()
    return render(request, 'accounts/signup.html', {'form' : form})


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request = request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                messages.info(request, "user login successfull")
                return redirect('core:index')
            else:
                messages.error(request, "invalid username and password combination")
        else:
            messages.error(request, "invalid username and password combination")
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', context={'form' : form})

def logout_view(request):
    logout(request)
    messages.info(request, "logged out successfull")
    return redirect('core:index')