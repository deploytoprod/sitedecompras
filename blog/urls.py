from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.models import User

urlpatterns = patterns('',
    url(r'^$', 'blog.views.posts'), #/blog/
    url(r'^post/(?P<id>\d+).python$', 'blog.views.post'), #/blog/
)
