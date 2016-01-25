from django.views.generic import TemplateView
from django.http import Http404
from utils import load_md_file, get_page_by_attr


class MarkdownPageView(TemplateView):
    template_name = "base_md_file.html"

    def get(self, *args, **kwargs):
        self.page = get_page_by_attr('path', kwargs.get('path', ''))
        if not self.page:
            raise Http404
        return super(MarkdownPageView, self).get(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        return {
            "content": load_md_file(self.page['markdown_file'])
        }
