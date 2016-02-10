from django.conf.urls import include, patterns, url
from django.contrib import admin

from .views import HomepageView

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^/?$', HomepageView.as_view(), name='homepage'),
    url(r'', include('api_docs.urls')),
)
