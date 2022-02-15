from django.shortcuts import render
from django.views.generic.list import Listview
from django.views.generic import DetailView


class PostListView(ListView):

class PostDetailView(DetailView):
    model = Post
    fields = ['__all__']
