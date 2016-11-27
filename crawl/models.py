from __future__ import unicode_literals

from django.db import models

class ContentIdentifier(models.Model):
	dom=models.CharField(max_length=30)
	css_selector=models.CharField(max_length=100,blank=True)

	def __str__(self):
		if self.css_selector:
			return str(self.dom)+' class='+str(self.css_selector)
		else:
			return str(self.dom)

class Input(models.Model):
	name=models.CharField(max_length=100)
	created_on=models.DateTimeField(auto_now=True)
	updated_on=models.DateTimeField(auto_now=True)
	url=models.CharField(max_length=300)
	processed=models.BooleanField(default=False)
	category_container_identifier=models.ForeignKey(ContentIdentifier,related_name='category_container_identifier')
	category_name_identifier=models.ForeignKey(ContentIdentifier,related_name='category_name_identifier')
	category_title_identifier=models.ForeignKey(ContentIdentifier,related_name='category_title_identifier')
	category_summary_identifier=models.ForeignKey(ContentIdentifier,related_name='category_summary_identifier')
	post_container_identifier=models.ForeignKey(ContentIdentifier,related_name='post_container_identifier')
	post_title_identifier=models.ForeignKey(ContentIdentifier,related_name='post_title_identifier')
	post_summary_identifier=models.ForeignKey(ContentIdentifier,related_name='post_summary_identifier')
	post_link_identifier=models.ForeignKey(ContentIdentifier,related_name='post_link_identifier')

	def __str__(self):
		return self.name

class Post(models.Model):
	title=models.CharField(max_length=200)
	summary=models.TextField()
	link=models.CharField(max_length=300)
	input=models.ForeignKey(Input,on_delete=models.CASCADE)

class Category(models.Model):
	name=models.CharField(max_length=100)
	title=models.CharField(max_length=200)
	summary=models.TextField()
	created_on=models.DateTimeField(auto_now=True)
	updated_on=models.DateTimeField(auto_now=True)
	posts=models.ManyToManyField(Post)