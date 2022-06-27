from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm

def post_list(request):
	posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})


def post_detail(request, pk):
	post=get_object_or_404(Post,pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})


def post_new(request):
	# if this is a POST request we need to process the form data
	if request.method == "POST":
		# create a form instance and populate it with data from the request:
		# This is called “binding data to the form” (it is now a bound form)
		form=PostForm(request.POST)
		
		# If is_valid() is True, we’ll now be able to find all the validated form data in its cleaned_data attribute.
		# We can use this data to update the database or
		# do other processing before sending an HTTP redirect to the browser telling it where to go next.
		if form.is_valid():
			post=form.save(commit=False)
			post.author=request.user
			post.published_date=timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)

    # if a GET (or any other method) we'll create a blank form
	else:
		form=PostForm()
		return render(request, 'blog/post_edit.html', {'form':form})



def post_edit(request, pk):
	post=get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form=PostForm(request.POST, instance=post)
		if form.is_valid():
			post=form.save(commit=False)
			post.author=request.user
			post.published_date=timezone.now()
			post.save()
			return redirect('post_detail',pk=post.pk)

	else:
		form=PostForm(instance=post)
	return render(request,'blog/post_edit.html',{'form':form})





	
