from django.shortcuts import render, redirect
from .models import Post
# from .models import Tag
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.contrib import messages
import smtplib
from smtplib import *

def home(request):
	context = {
		'posts': Post.objects.all(),
	}
	
	return render(request, "blog/home.html", context)

def about(request):
	return render(request, "blog/about.html")


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['morgan.waites@gmail.com'])
            except BadHeaderError:
            	return HttpResponse('Invalid header found.')
            except SMTPResponseException as e:
            	return HttpResponse('Email contact is not functional currently. Apologies.')
            messages.success(request, "Thank you for contacting us. Your email has been sent.")
            return redirect('site-help')
        


    return render(request, "blog/help.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')


def explore(request):

	return render(request, "blog/explore.html")

def SearchResults(request):
	if request.method == "GET":
		searched = request.GET.get('searched')
		#take away capitalizations and search lowercase versions as well with lower() method
		searchedL=searched.lower()
		context = {'searched': searched, 'post_results': []} 
		all_posts = Post.objects.all()
		for post in all_posts:
			found=False
			list_of_words_in_title = post.title.lower().split() #splits words in title into list
			for word in list_of_words_in_title:
				if word==searchedL:
					found=True
			if found==False:
				list_of_words_in_content = post.post_content.lower().split()
				for word in list_of_words_in_content:
					if word==searchedL:
						found=True
			if found==False:
				author = post.author.username
				if author==searched:
						found=True
			if found:
				context['post_results'].append(post)

	
		return render(request, "blog/search_results.html", context)






	else:
		return render(request, "blog/search_results.html", {})
# class MultipleModelView(TemplateView):
#     template_name = 'blog/home.html'
    
#     def get_context_data(self, **kwargs):
#          context = super(MultipleModelView, self).get_context_data(**kwargs)
#          context['posts'] = Post.objects.all().order_by('-date_posted')
#          context['tags'] = Tag.objects.all()
#          return context

class PostListView(ListView):
	#MultipleModelsListView(ListView) - add in Tag, look up context object name multiple too, 
	#feed into home.html 
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostUserListView(ListView):
	model = Post

	def get_queryset(self):
		posts = Post.objects.all()
		for post in posts:
			if post.author.username==self.kwargs['username']:
				pk_value=post.author.id
				break
		queryset = Post.objects.all().filter(author=pk_value)
		queryset=queryset.order_by('-date_posted')
		return queryset
	template_name = 'blog/user_blog.html'
	

	

class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'
	# def get_context_data(self, **kwargs):
 #         context = super(PostDetailView, self).get_context_data(**kwargs)
 #         context['posts'] = Post.objects.all().order_by('-date_posted')
 #         context['tags'] = Tag.objects.all()
 #         return context


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
