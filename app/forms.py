from django import forms
from app.models import Thread, Post

class ThreadForm(forms.ModelForm):
	title = forms.CharField(widget = forms.TextInput(attrs={
		'placeholder': 'Your title here'
		}), max_length = 200)
	text = forms.CharField(widget = forms.Textarea(attrs={
		'placeholder':'Enter your fucking text here...'
		}), max_length = 4962)

	class Meta:
		model = Thread
		fields = ['title', 'text']

class PostForm(forms.ModelForm):
	text = forms.CharField(widget = forms.Textarea, max_length = 4962)

	class Meta:
		model = Post
		fields = ['text']

