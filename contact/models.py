from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.contrib.auth.models import User


# Create your models here.

class update(models.Model):
	name = models.CharField(max_length=120)
	user_id = models.OneToOneField(User, on_delete=models.CASCADE, default='update', null=True)
	avatar = models.ImageField(default='default.jpg', upload_to='profile_pics')
	description = models.TextField(default='description default value')
	location = models.TextField(default='my location')
	created_at = models.DateTimeField(auto_now=True)



	def __str__(self):
		return self.name

