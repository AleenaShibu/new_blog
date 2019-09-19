from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Post

class HomePostView(ListView):
	model = Post
	template_name = 'index.html'

class DetailPostView(DetailView):
	model = Post
	template_name = 'details.html'

class AddPostView(CreateView):
	model = Post
	template_name = 'addpost.html'
	fields = ['title','content']

class UpdatePostView(UpdateView):
	model = Post
	template_name = 'update.html'
	fields = ['title','content']

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete.html'
	success_url = reverse_lazy('lists')