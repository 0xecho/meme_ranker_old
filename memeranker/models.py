from django.db import models

# Create your models here.

class Meme(models.Model):
	
	uploader = models.CharField(default='0xecho',max_length=120)
	image = models.ImageField(upload_to='memes/%Y/%m/%d')
	likes = models.IntegerField(default=0)

	def __str__(self):
		return self.image.name
	
