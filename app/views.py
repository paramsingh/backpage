from django.shortcuts import render
from app.forms import ThreadForm
from app.models import Thread
from django.http import HttpResponseRedirect, HttpResponse


def create(request):
	context_dict = {'form': ThreadForm()}
	if request.method == 'POST':
		form = ThreadForm(request.POST)
		if form.is_valid():
			thread = form.save(commit=True)
			return HttpResponseRedirect("/app/thread/"+str(thread.id)+"/")
	return render(request, 'app/create_thread.html', context_dict)

def thread(request, thread_id):
	thread_id = int(thread_id)
	thread = Thread.objects.get(id=thread_id)
	if not thread:
		return HttpResponse("404")
	context_dict = {'thread': thread}
	return render(request, 'app/thread.html', context_dict)



