from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

from .views import HomepageView


# Redirect views
urlpatterns = [
    url(
        r'^{}(\/?)$'.format(src),
        RedirectView.as_view(url=dst, permanent=True)
    ) for src, dst in settings.REDIRECTS
]

urlpatterns += [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomepageView.as_view(), name='homepage'),
    url(r'', include('api_docs.urls')),
]
