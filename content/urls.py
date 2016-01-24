from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^', views.HomePageView.as_view(), name='home')
)
