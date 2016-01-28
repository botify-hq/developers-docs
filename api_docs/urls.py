from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'/datamodel', views.DatamodelView.as_view(), name='datamodel'),
    url(r'/swagger', views.SwaggerUiView.as_view(), name='swagger-ui'),
    url(r'(?P<path>.+)', views.MarkdownPageView.as_view(), name='md-page')
)
