from django.db import models

# Create your models here.
class Post(models.Model):
	context = models.TextField()
	def __str__(self):
		""" represent models using context"""
		return self.context[:50]