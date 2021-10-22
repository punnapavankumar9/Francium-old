from django import core
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserSignUpForm, UserLoginForm, UserProfileForm, UserUpdateForm
from .models import UserPofile
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

@login_required
def profile_view(request, username):
    if(request.method == 'POST'):
        if(request.user.username == username):
            usr_form = UserUpdateForm(request.POST)
            profile_form = UserProfileForm(request.POST)
            if(usr_form.is_valid() and profile_form.is_valid()):
                usr_form.save()
                profile_form.save()
                messages.success(request, "Profile updated successfully.")
                return redirect('accounts:profile')
        else:
            messages.warning(request, "You don't access to the profile")
            return redirect('core:index')
    else:
        if(request.user.username == username):
            user = User.objects.get(username = username)
            usr_form = UserUpdateForm(instance = user)
            profile_form = UserProfileForm(instance=user.profile)
            context = {}
            context['perm'] = True
            context['usr_form'] = usr_form
            context['profile_form'] = profile_form
            context['name'] = "punnasd"
            return render(request, 'accounts/profile.html', context)
        else:
            context = {}
            context['perm'] = False
            user_profile = UserPofile.objects.get(user__username = username)
            
            context['user_profile'] = user_profile
            return render(request, 'accounts/profile.html', context)