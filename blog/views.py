from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# def home(request):
#     context = {}
#     return render(request, 'blog/home.html', context)


class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'