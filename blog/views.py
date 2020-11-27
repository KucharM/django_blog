from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class CreatePostView(CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    fields = '__all__'
    success_url = reverse_lazy('blog:home')