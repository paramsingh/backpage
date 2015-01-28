from app.models import Thread, Post

for i in Thread.objects.all():
	print("Updating post count")
	i.post_count = Post.objects.filter(thread = i).count()
	i.save()