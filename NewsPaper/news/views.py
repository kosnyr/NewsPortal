from datetime import datetime

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(
        category_type='NW'
    ).order_by('id')
    template_name = 'news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next_sale'] = None
        return context


class PostDetail(DetailView):
    model = Post
    queryset = Post.objects.filter(
        category_type='NW'
    ).order_by('id')
    template_name = 'one_news.html'
    context_object_name = 'one_news'
