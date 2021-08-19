from django.shortcuts import render
#from django.http import HttpResponse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages

def home(request):
	context = {
		'posts': Post.objects.all(),
	}
	
	return render(request, "blog/home.html", context)

def about(request):
	return render(request, "blog/about.html")

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostUserListView(ListView):
	model = Post

	def get_queryset(self):
  		queryset = set()
  		for p in Post.objects.all():
  			if p.author.username==self.kwargs['username']:
  				queryset.add(p)
  		#go into shell figure out how to reoder queryset bt date
  		return queryset
	template_name = 'blog/user_blog.html'
	

		

class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'post_content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'post_content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post=self.get_object()
		if self.request.user == post.author:
			return True
		return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

	model = Post
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post=self.get_object()
		if self.request.user == post.author:
			return True
		return False
	def get_success_url(self):
		messages.add_message(self.request, messages.INFO, 'Post deleted.')
		return reverse('profile')
