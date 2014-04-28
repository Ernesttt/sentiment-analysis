from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from comments import views

urlpatterns = patterns('',
    url(r'^comments$', views.CommentsSentiment.as_view()),
    #url(r'^comments/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)