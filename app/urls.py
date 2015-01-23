from django.conf.urls import patterns, url
from app import views

urlpatterns = patterns('',
	url(r'^create/$', views.create, name="create_thread"),
	url(r'^thread/(?P<thread_id>\w+)/$', views.thread, name="view thread"),
	url(r'^numposts/(?P<thread_id>\w+)/$', views.numberofposts, name="numberofposts"),
	url(r'^test/$', views.test, name="test"),
	url(r'^index/$', views.all_threads, name="all")
)