from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_pic = models.ImageField(default='anon.png', upload_to='profile-pics')

def __str__(self):
	return f'{self.user.username} Profile'



