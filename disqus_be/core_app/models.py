"""This module contains DB models"""
from django.db import models
from django.utils import timezone
from core_app import utils
from hashlib import md5

class Comment(models.Model):
	author = models.CharField(max_length=30)
	text = models.CharField(max_length=30)
	pub_date = models.DateField(auto_now=True)
	link = models.CharField(max_length=30)