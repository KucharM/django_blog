from django.urls import path
from .views import HomeView, PostDetailView, CreatePostView


app_name = 'blog'

urlpatterns = [
    path('posts/', HomeView.as_view(), name='home'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/create_post/', CreatePostView.as_view(), name='create_post')
]
