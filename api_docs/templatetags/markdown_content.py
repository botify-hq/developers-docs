from django import template
from django.utils.safestring import mark_safe
from ..utils import load_md_file

register = template.Library()


@register.simple_tag
def md_content(path):
    """
    :param path: relative path (to the markdowns folder) of the markdown file
    :type path: string
    :return : string
    retrieves the content of a markdown file transformed into html
    """
    try:
        return mark_safe(load_md_file(path))
    except IOError:
        return None
