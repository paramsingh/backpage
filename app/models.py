from django.db import models


class Thread(models.Model):
	global_thread_num = 0
	title = models.CharField(max_length=200)
	thread_pos = models.IntegerField(default=1)
	text = models.TextField(default='')
	submitter = models.CharField(max_length=50, null=True)

	def op(self):
		return self.posts.first()
	def __str__(self):
		return self.title

class Post(models.Model):
	global_post_num = 0
	time_posted = models.DateTimeField(auto_now_add=True)
	text = models.TextField(default='')
	thread = models.ForeignKey('Thread', related_name='posts')
	submitter = models.CharField(max_length=50, null=True)
	post_num = models.IntegerField(null=True)

	def __init__(self):
		Post.global_post_num += 1
		self.post_num = Post.global_post_num

