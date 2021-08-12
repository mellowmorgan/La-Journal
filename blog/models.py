from django.db import models
from django.utils import timezone
from django.utils import timezone
timezone.localtime(timezone.now())
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	post_content = models.TextField(max_length=10000)
	date_posted= models.DateTimeField(auto_now_add=True)
	#DateTimeField(auto_now_add) or try timezone.now()ß
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
