import os
import markdown2
from markdown import markdown
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "base.html"

    def get_context_data(self):
        f = open("{}/markdowns/homepage.md".format(
            os.path.dirname(os.path.abspath(__file__))
        ), "r")
        content = f.read()
        f.close()
        extensions = [
            'markdown.extensions.abbr',
            'markdown.extensions.attr_list',
            'markdown.extensions.def_list',
            'markdown.extensions.fenced_code',
            'markdown.extensions.footnotes',
            'markdown.extensions.tables',
            'markdown.extensions.smart_strong',
            'markdown.extensions.admonition',
            'markdown.extensions.codehilite',
            'markdown.extensions.headerid',
            'markdown.extensions.meta',
            'markdown.extensions.nl2br',
            'markdown.extensions.sane_lists',
            'markdown.extensions.smarty',
            'markdown.extensions.toc',
            'markdown.extensions.wikilinks'
        ]
        return {
            "content": markdown(content, extensions=extensions),
            "content2": markdown2.markdown(content)
        }
