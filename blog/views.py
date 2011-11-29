from models import Post, Comment
from django.shortcuts import render #com esse cara nao preciso retornar o HttpResponse e nem importar o get_template nem o HttpResponse, nem o Template, nem o Context (linha acima), vou fazer no posts pra ver (BACANA!)

def posts(request):
	posts = Post.objects.all()
	return render(request, 'blog/posts.html', locals())

def post(request, id):
	posts = Post.objects.all()
	post = Post.objects.get(id=id)
	comments = Comment.objects.filter(post = post, approved = True)
	
	teve_comentario = False
	if request.method == 'POST':
		teve_comentario = True
		comment = Comment()
		comment.post = post
		comment.name = request.POST['nome']
		comment.email = request.POST['email']
		comment.comment = request.POST['comentario']
		comment.save()
		
	return render(request, 'blog/post.html', locals())