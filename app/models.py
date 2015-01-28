from django.db import models

class Thread(models.Model):
	title = models.CharField(max_length=200)
	thread_pos = models.IntegerField(default=1)
	text = models.TextField(default='')
	time = models.DateTimeField(auto_now_add=True, null=True)
	last_post_time = models.DateTimeField(auto_now_add=True, null=True)
	reports = models.IntegerField(default = 0)
	post_count = models.IntegerField(default = 0)
	poster = models.GenericIPAddressField(null=True)
	admin = models.BooleanField(default = False)

	
	def __str__(self):
		return self.title

class Post(models.Model):
	time_posted = models.DateTimeField(auto_now_add=True)
	text = models.TextField(default='')
	reports = models.IntegerField(default = 0)
	thread = models.ForeignKey('Thread', related_name='posts')
	poster = models.GenericIPAddressField(null=True)
	admin = models.BooleanField(default = False)


	def __str__(self):
		return self.text

class ThreadReport(models.Model):
	thread = models.ForeignKey('Thread')
	message = models.CharField(max_length = 500, default = '')

	def __str__(self):
		return self.message

class PostReport(models.Model):
	post = models.ForeignKey('Post')
	message = models.CharField(max_length = 500, default = '')

	def __str__(self):
		return self.message
