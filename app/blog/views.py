from django.shortcuts import render
from .forms import CommentForm
from blog.models import Post, Comment


def blog_index(request):

	posts = Post.objects.all().order_by('-created_on')

	return render(request, "blog_index.html", {'posts':posts})


def blog_category(request, category):

	posts = Post.objects.filter(
		categories__name__contains=category
	).order_by(
		'-created_on'
	)

	context = {
		"category" : category,
		"posts" : posts
	}
	return render(request, "blog_category.html", context)

def blog_detail(request, pk):

	#get the post object from the DB
	post = Post.objects.get(pk=pk)

	#if the request is post then there will be a new comment
	#so we save this to the database
	form = CommentForm()
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = Comment(

				author=form.cleaned_data['author'],
				body=form.cleaned_data['body'],
				post=post

			)
			comment.save()

	#get all the comments for this post
	comments = Comment.objects.filter(post=post)
	
	#render this as a template
	context = {
		"post": post,
		"comments" : comments,
		"form": form,

	}
	return render(request, "blog_detail.html", context)