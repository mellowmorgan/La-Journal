from django.shortcuts import render
#from django.http import HttpResponse
from .models import Post

def home(request):
	context = {
		'posts': Post.objects.all(),
		'listy': [1,2,3,4,5,6,7,8,9],
	}
	

	return render(request, "blog/home.html", context)

def about(request):
	return render(request, "blog/about.html")