from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserPofile

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

    def __init__(self, *args, **kwargs):
        super(UserSignUpForm, self).__init__(*args, **kwargs) 
        self.fields['username'].widget.attrs.update({'class': 'form_input', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'class': 'form_input', 'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'class': 'form_input', 'placeholder': 'password'})
        self.fields['password2'].widget.attrs.update({'class': 'form_input', 'placeholder': 'confirm password'})

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, ** kwargs)
        self.fields['password'].widget.attrs.update({'class': 'form_input', 'placeholder': 'Password'})
        self.fields['username'].widget.attrs.update({'class': 'form_input', 'placeholder': 'Username'})


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form_input', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update({'class': 'form_input','type':"email" , 'placeholder': 'Email'})
        self.fields['first_name'].widget.attrs.update({'class': 'form_input', 'placeholder': 'first name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form_input', 'placeholder': 'last name'})

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserPofile
        fields = ['gender', 'profile_pic']