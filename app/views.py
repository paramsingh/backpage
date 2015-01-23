from django.shortcuts import render
from app.forms import ThreadForm, PostForm
from app.models import Thread, Post
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core import serializers


def create(request):
	context_dict = {'form': ThreadForm()}
	if request.method == 'POST':
		thread_form = ThreadForm(request.POST)
		if thread_form.is_valid():
			thread = thread_form.save(commit=True)
			return HttpResponseRedirect("/app/thread/"+str(thread.id)+"/")
		else:
			print(thread_form.errors)
	return render(request, 'app/create_thread.html', context_dict)

def thread(request, thread_id):
	thread_id = int(thread_id)
	try:
		current_thread = Thread.objects.get(id=thread_id)
	except Thread.DoesNotExist:
		return HttpResponse("404 Thread does not exist")
	context_dict = {'thread': current_thread}
	if request.method == 'POST':
		post_form = PostForm(request.POST)
		if post_form.is_valid():
			post = post_form.save(commit = False)
			post.thread = current_thread
			post.save()
		else:
			print(post_form.errors)
	context_dict['post_form'] = PostForm()
	context_dict['posts'] = Post.objects.filter(thread = current_thread)
	context_dict['num_posts'] = len(context_dict['posts'])
	return render(request, 'app/thread.html', context_dict)

def numberofposts(request, thread_id):
	thread_id = int(thread_id)
	try:
		current_thread = Thread.objects.get(id=thread_id)
	except Thread.DoesNotExist:
		return HttpResponse("404 Thread does not exist")
	posts = Post.objects.filter(thread = current_thread)
	dict_posts = {}
	for i in posts:
		dict_posts[i.id] = {'text':i.text, 'time': i.time_posted}

	return JsonResponse(dict_posts)

def test(request):
	return render(request, 'app/test.html', {})


