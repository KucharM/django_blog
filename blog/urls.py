from django.urls import path
from .views import HomeView, PostDetailView


app_name = 'blog'

urlpatterns = [
    path('posts/', HomeView.as_view(), name='home'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
