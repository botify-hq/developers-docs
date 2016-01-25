from django.views.generic import TemplateView
from django.http import Http404
from utils import load_md_file
from .index import PAGES


class MarkdownPageView(TemplateView):
    template_name = "base_md_file.html"

    def get(self, *args, **kwargs):
        self.page = filter(
            lambda x: x['path'] == kwargs.get('path', ''),
            PAGES)
        if not self.page:
            raise Http404
        self.page = self.page[0]
        return super(MarkdownPageView, self).get(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        return {
            "content": load_md_file(self.page['markdown_file'])
        }