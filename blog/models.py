from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=50)
	
	class Meta:
		verbose_name = u'Categoria'
		verbose_name_plural = u'Categorias'
	
	def __unicode__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length = 100)
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
	
	class Meta:
		verbose_name = u'Comentario'
		verbose_name_plural = u'Comentarios'
	
	def __unicode__(self):
		return self.comment