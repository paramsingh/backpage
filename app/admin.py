from django.contrib import admin
from app.models import Thread, Post, ThreadReport, PostReport
# Register your models here.
class ThreadAdmin(admin.ModelAdmin):
	fields = ('title', 'text', 'reports')
	list_display = ('title', 'reports')

class PostAdmin(admin.ModelAdmin):
	fields = ('text', 'thread', 'reports')
	list_display = ('text', 'thread', 'reports')

class ThreadReportAdmin(admin.ModelAdmin):
	fields = ('message', 'thread')
	list_display = ('message', 'thread')

class PostReportAdmin(admin.ModelAdmin):
	fields = ('message', 'post')
	list_display = ('message', 'post')

admin.site.register(ThreadReport, ThreadReportAdmin)
admin.site.register(PostReport, PostReportAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post, PostAdmin)