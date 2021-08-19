from django.db import models
from PIL import Image
from PIL import ExifTags, ImageOps
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_pic = models.ImageField(default='anon.png', upload_to='profile-pics')

	def __str__(self):
		return "{} Profile".format(self.user.username)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		img = Image.open(self.profile_pic.path)
	
		if img.height > 500 or img.width > 500:
			if img.height > img.width:
				factor=500/img.height
				nH=500
				nW=img.width*factor
				output_size= (nH,nW)
			if img.width > img.height:
				factor=500/img.width
				nW=500
				nH=img.height*factor
				output_size= (nH,nW)
			else:
				output_size=(500,500)

			img = ImageOps.exif_transpose(img)
		
			img.thumbnail(output_size)
			img.save(self.profile_pic.path) 
	

#get tuple of h, w tupe using shape t[0]=h t[1]=w find out which which put into variables then figure out how to resize re aspect ratio put here
#if h greater than width, if h bigger than 500 do resize with percentages

#1000x400

#whatever to get down to 500 .5*original resize down .5x original 

#vice versa, both need to be less than 500, do too if/else one for width one for heigh