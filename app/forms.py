from django import forms
from app.models import Thread, Post, ThreadReport, PostReport

class ThreadForm(forms.ModelForm):
	title = forms.CharField(widget = forms.TextInput(attrs={
		'placeholder': 'Your title here'
		}), max_length = 200)
	text = forms.CharField(widget = forms.Textarea(attrs={
		'placeholder':'Enter your text here...'
		}), max_length = 4962)

	class Meta:
		model = Thread
		fields = ['title', 'text']

class PostForm(forms.ModelForm):
	text = forms.CharField(widget = forms.Textarea, max_length = 4962)

	class Meta:
		model = Post
		fields = ['text']

class PostReportForm(forms.ModelForm):
	message = forms.CharField(max_length = 500)

	class Meta:
		model = PostReport
		fields = ['message']

class ThreadReportForm(forms.ModelForm):
	message = forms.CharField(max_length = 500)
	class Meta:
		model = ThreadReport
		fields = ['message']

