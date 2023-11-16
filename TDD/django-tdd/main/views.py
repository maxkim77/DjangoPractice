from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q
from .models import Post

class MainPageView(TemplateView):
    template_name = 'main/index.html'    

class AboutPageView(TemplateView):
    template_name = 'main/about.html'

class ContactPageView(TemplateView):
    template_name = 'main/contact.html'

class BlogListView(ListView):
    model = Post
    template_name = 'main/blog.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'main/post.html'
    context_object_name = 'post'

class BlogSearchView(ListView):
    model = Post
    template_name = 'main/blog.html'
    context_object_name = 'posts'

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()