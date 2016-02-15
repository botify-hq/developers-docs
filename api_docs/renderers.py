from django_medusa.renderers import StaticSiteRenderer
from .markdowns.index import PAGES
from utils import reverse_page


class APIMdDocsRenderer(StaticSiteRenderer):
    def get_paths(self):
        api_md_pages_paths = [reverse_page(page['url_name']) for page in PAGES]
        return frozenset(api_md_pages_paths)


class StaticDjangoRenderer(StaticSiteRenderer):

    EXCLUDED_PATTERNS = [
        'md-page'
    ]

    def get_paths(self):
        from .urls import urlpatterns
        paths = ['/']
        for pattern in urlpatterns:
            if pattern.name not in self.EXCLUDED_PATTERNS:
                url = reverse_page(pattern.name)
                url += "/" if not url.endswith("/") else ""
                paths.append(url)
        return frozenset(paths)


renderers = [APIMdDocsRenderer, StaticDjangoRenderer]
