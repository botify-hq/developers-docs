from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'api/reference/$', views.SwaggerUiView.as_view(), name='reference'),
    url(r'api/analysis/urls-datamodel/$', views.DatamodelView.as_view(), name='analysis-urls-datamodel'),
    url(r'404/$', views.NotFoundView.as_view(), name='404'),
    url(r'(?P<path>.+)/$', views.MarkdownPageView.as_view(), name='md-page'),
)
