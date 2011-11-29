from django.db import models 

class Contato(models.Model):
	nome = models.CharField(max_length = 60)
	email = models.EmailField(max_length = 60)
	assunto = models.TextField()
	mensagem = models.TextField(null=True)
	mensagem2 = models.TextField(null=True)
	#sexo = models.CharField(max_length=1, choices=(('M','Masculino'),('F','Femenino')))
	
	def __unicode__(self):
		return u'%s' % (self.nome)
