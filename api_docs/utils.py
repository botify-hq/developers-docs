# -*- coding: utf-8 -*-
import os
from markdown import markdown
from .index import PAGES


def get_markdown_content(md_file):
    """
    :param md_file: filename (path) to the markdown file
    :type md_file: string
    :return : string
    Searches a file in the markdowns/ folder and returns its contents
    """
    f = open("{base}/markdowns/{file}".format(
        base=os.path.dirname(os.path.abspath(__file__)),
        file=md_file
    ), "r")
    content = f.read()
    f.close()
    return content


def md2html(content):
    """
    :param content: markdown content
    :type content: string
    :return : string
    converts markdown content to html
    """
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
        'api_docs.md_extensions'
    ]
    return markdown(content, extensions=extensions)


def load_md_file(md_file):
    """
    :param md_file: filename (path) to the markdown file
    :type md_file: string
    :return : string
    """
    content = get_markdown_content(md_file)
    html = md2html(content)
    return html


def get_page_by_attr(attr_name, attr_value):
    """
    :param attr_name: attribute to search
    :type attr_name: string
    :param attr_value: value to search
    :type attr_value: string
    :return : dict
    searches a definition in the PAGES constant and returns
    the first matchet element
    """
    try:
        return next(page for page in PAGES if page[attr_name] == attr_value)
    except StopIteration:
        return None
