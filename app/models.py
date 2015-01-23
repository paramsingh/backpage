from django.db import models


class Thread(models.Model):
	global_thread_num = 0
	title = models.CharField(max_length=200)
	thread_pos = models.IntegerField(default=1)
	text = models.TextField(default='')
	time = models.DateTimeField(auto_now_add=True, null=True)
	last_post_time = models.DateTimeField(auto_now_add=True, null=True)

	
	def __str__(self):
		return self.title

class Post(models.Model):
	time_posted = models.DateTimeField(auto_now_add=True)
	text = models.TextField(default='')
	thread = models.ForeignKey('Thread', related_name='posts')

