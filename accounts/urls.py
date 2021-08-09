from django.urls import path
from .views import signup_view, login_view, logout_view, profile_view

app_name = 'accounts'


urlpatterns = [
    path('register/', signup_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/<str:username>/', profile_view, name='profile'),

]