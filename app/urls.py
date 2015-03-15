from django.conf.urls import patterns, url
from app import views

urlpatterns = patterns('',
	url(r'^index/$', views.index, name="create_thread"),
	url(r'^thread/(?P<thread_id>\w+)/$', views.thread, name="view thread"),
	url(r'^numposts/(?P<thread_id>\w+)/$', views.numberofposts, name="numberofposts"),
	url(r'^report_thread/(?P<thread_id>\w+)/$', views.report_thread, name="report_thread"),
	url(r'^report_post/(?P<post_id>\w+)/$', views.report_post, name="report_post"),
	url(r'^post/(?P<post_id>\w+)/$', views.post_redirect, name="post_redirect")
)
