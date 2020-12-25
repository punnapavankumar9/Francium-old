from .views import home, about, PostDetailView,PostsListView, PostCreateView, PostDeleteView, PostUpdateView, UserPostListView
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', PostsListView.as_view(), name="home"),
    path('about/', about, name="about"),
    path('detail/<int:pk>/', PostDetailView.as_view(), name="detail"),
    path('create/', PostCreateView.as_view(), name="create"),
    path('update/<int:pk>/', PostUpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name="delete"),
    path('user/<str:username>/', UserPostListView.as_view(), name="user-posts"),
]
