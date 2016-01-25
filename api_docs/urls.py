from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'(?P<path>.+)', views.MarkdownPageView.as_view(), name='md-page')
)
