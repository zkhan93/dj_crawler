from __future__ import unicode_literals

from django.db import models

class ContentIdentifier(models.Model):
	dom=models.CharField(max_length=30)
	css_selector=models.CharField(max_length=100)

class Input(models.Model):
	name=models.CharField(max_length=100)
	created_on=models.DateTimeField(auto_now=True)
	updated_on=models.DateTimeField(auto_now=True)
	url=models.CharField(max_length=300)
	content_identifiers=models.ManyToManyField(ContentIdentifier)

class Post(models.Model):
	title=models.CharField(max_length=200)
	summary=models.TextField()
	link=models.CharField(max_length=300)
	input=models.ForeignKey(Input,on_delete=models.CASCADE)

class Category(models.Model):
	category=models.CharField(max_length=100)
	title=models.CharField(max_length=200)
	summary=models.TextField()
	created_on=models.DateTimeField(auto_now=True)
	updated_on=models.DateTimeField(auto_now=True)
	posts=models.ManyToManyField(Post)