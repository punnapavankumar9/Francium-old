from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import fields

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
