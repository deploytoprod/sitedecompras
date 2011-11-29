from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=100)
	post = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	last_modified = models.DateTimeField(auto_now = True)
	categories = models.ManyToManyField('Category')

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	post = models.ForeignKey('Post') #cria FK referenciando o Post
	email = models.EmailField()
	name = models.CharField(max_length=60)
	comment = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	approved = models.BooleanField(default = False)
	
	def __unicode__(self):
		return self.comment

class Category(models.Model):
	name = models.CharField(max_length=50)
	
	def __unicode__(self):
		return self.name