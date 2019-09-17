from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post

class HomePostView(ListView):
	model = Post
	template_name = 'index.html'

class DetailPostView(DetailView):
	model = Post
	template_name = 'details.html'