from django import forms
from app.models import Thread, Post

class ThreadForm(forms.ModelForm):
	title = forms.CharField(max_length = 200)
	text = forms.CharField(max_length = 4962)
	submitter = forms.CharField(max_length = 50)

	class Meta:
		model = Thread
		fields = ['title', 'text', 'submitter']

