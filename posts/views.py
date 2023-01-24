from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
    )
    from django.urls import reverse_lazy

    from .models import Post

    class PostListView(ListView):




    class PostDetailView(DeleteView):




    class PostCreateView(CreateView):


class PostListView(ListView):
    template_name = "posts/list.html"
    model = =Post
    fields = ["title", "subtitle", "body"]

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post
    success_url = reverse_lazy("list")



class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "author", "body"]


# Create your views here.
