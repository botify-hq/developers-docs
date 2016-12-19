from django.views.generic import TemplateView
from django.http import Http404
from django.conf import settings
from utils import load_md_file, get_page_by_attr, reverse_page


class MarkdownPageView(TemplateView):
    template_name = "base/base_md_file.html"

    def get(self, *args, **kwargs):
        self.page = get_page_by_attr('path', kwargs.get('path', ''))
        if not self.page:
            raise Http404
        return super(MarkdownPageView, self).get(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        properties = self.page.get('properties', {})
        breadcrumb = []
        for page_name in properties.get('breadcrumb', []):
            page = get_page_by_attr('url_name', page_name)
            title = (page['properties']['title']
                     if 'properties' in page and 'title' in page['properties']
                     else "")
            breadcrumb.append({
                'link': reverse_page(page_name),
                'name': title
            })

        context = {
            "properties": properties,
            "breadcrumb": breadcrumb
        }

        if 'markdown_file' in self.page:
            context['content'] = load_md_file(self.page['markdown_file'])
            context['markdown_file'] = self.page['markdown_file']

        if 'redirect_path' in self.page:
            context['redirect_path'] = '/%s/' % self.page['redirect_path']

        return context


class AnalysisDatamodelView(TemplateView):
    template_name = "analysis_datamodel.html"

    def get_context_data(self, *args, **kwargs):
        return {
            "datamodel_api_url": settings.ANALYSIS_DATAMODEL_API_URL,
            "properties": {
                "menu_item": "analysis-datamodel",
                "breadcrumb": ["analysis"],
                "title": "Analysis | URLs Datamodel",
                "description": "Botify API, URLs Datamodel"
            }
        }

class LogsDatamodelView(TemplateView):
    template_name = "logs_datamodel.html"

    def get_context_data(self, *args, **kwargs):
        return {
            "datamodel_api_url": settings.LOGS_DATAMODEL_API_URL,
            "properties": {
                "menu_item": "logs-datamodel",
                "breadcrumb": ["logs"],
                "title": "Logs | URLs & Segments Datamodel",
                "description": "Botify API, URLs & Segments Datamodel"
            }
        }


class SwaggerUiView(TemplateView):
    template_name = "swagger_ui.html"

    def get_context_data(self, *args, **kwargs):
        return {
            "api_url": settings.SWAGGER_API_URL,
            "properties": {
                "menu_item": "reference",
                "breadcrumb": [],
                "title": "Reference",
                "description": "Botify API Reference"
            }
        }


class NotFoundView(TemplateView):
    template_name = "404.html"

    def get_context_data(self, *args, **kwargs):
        return {
            "properties": {
                "title": "404 - Page Not Found",
                "description": "Not all those who wander are lost, J.R.R. Tolkien."
            }
        }
