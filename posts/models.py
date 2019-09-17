from django.db import models
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	author = models.TextField()
	def __str__(self):
		return self.title[ :50]

	def get_absolute_url(self):
		return reverse('detail', args=[str(self.id)])