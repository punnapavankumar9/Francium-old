from .views import register, profile
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static


app_name = 'accounts'

urlpatterns = [
    path('register/', register, name="register"),
    path('profile/', profile, name="profile"),
    path('login/', LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
] 