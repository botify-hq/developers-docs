from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'/datamodel', views.DatamodelView.as_view(), name='datamodel'),
    url(r'(?P<path>.+)', views.MarkdownPageView.as_view(), name='md-page')
)
