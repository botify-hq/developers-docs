from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'api/reference/$',
        views.SwaggerUiView.as_view(),
        name='reference'),

    url(r'api/analysis/datamodel/$',
        views.AnalysisDatamodelView.as_view(),
        name='analysis-datamodel'),

    url(r'api/logs/datamodel/$',
        views.LogsDatamodelView.as_view(),
        name='logs-datamodel'),

    url(r'404/$',
        views.NotFoundView.as_view(),
        name='404'),

    url(r'(?P<path>.+)/$',
        views.MarkdownPageView.as_view(),
        name='md-page'),
]
