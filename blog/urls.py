from django.conf.urls import url
from blog.views import *

# app_name = 'blog'
urlpatterns = [
    url(r'^$', PostList.as_view()),
    url(r'^post/(?P<slug>[-\w]+)/$', PostView.as_view(), name='post_view'),
    url(r'^category/(?P<slug>[-\w]+)/$', CategoryPostsList.as_view(), name='category_view'),
    url(r'^feedback/$', contact_form, name='contact'),
    url(r'^thanks/$', thanks, name='thanks'),

]
