'''
BotifyLinks Extension for Python-Markdown
======================================

Converts [[BotifyLinks]] to relative links.

'''
import re
from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
from markdown.util import etree
from .utils import reverse_page


BOTIFYLINK_RE = r'\[\[([^\[\]\;]+)\;([\w0-9_ -]+)(#?[\w0-9_ -]*)\]\]'


def build_url(label, base, end):
    """ Build a url from the label, a base, and an end. """
    clean_label = re.sub(r'([ ]+_)|(_[ ]+)|([ ]+)', '_', label)
    return '%s%s%s' % (base, clean_label, end)


class BotifyLinkExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        self.md = md

        # append to end of inline patterns
        pattern = BotifyLinks(BOTIFYLINK_RE, self.getConfigs())
        pattern.md = md
        md.inlinePatterns.add('botifylink', pattern, "<not_strong")


class BotifyLinks(Pattern):
    def __init__(self, pattern, config):
        super(BotifyLinks, self).__init__(pattern)
        self.config = config

    def handleMatch(self, m):
        link_text = m.group(2).strip()
        link_url_name = m.group(3).strip()
        link_anchor = m.group(4).strip()

        if not link_text or not link_url_name:
            return ''

        a = etree.Element('a')
        a.text = link_text

        a.set('href', "{}{}".format(
            reverse_page(link_url_name),
            link_anchor
        ))
        return a


def makeExtension(*args, **kwargs):
    return BotifyLinkExtension(*args, **kwargs)
