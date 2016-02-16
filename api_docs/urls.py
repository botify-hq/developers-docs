from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'api/urls-datamodel/$', views.DatamodelView.as_view(), name='urls-datamodel'),
    url(r'api/reference/$', views.SwaggerUiView.as_view(), name='reference'),
    url(r'(?P<path>.+)/$', views.MarkdownPageView.as_view(), name='md-page'),
)
