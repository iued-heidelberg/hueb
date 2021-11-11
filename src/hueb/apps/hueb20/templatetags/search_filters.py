from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()


@register.filter
def highlight_search(text, search):
    def replace_keep_case(word, text):
        def func(match):
            g = match.group()
            if g.islower():
                return "<mark>{}</mark>".format(word.lower())
            if g.istitle():
                return "<mark>{}</mark>".format(word.title())
            if g.isupper():
                return "<mark>{}</mark>".format(word.upper())
            return "<mark>{}</mark>".format(word)

        return re.sub(word, func, text, flags=re.I)

    for word in search:
        text = replace_keep_case(word, text)

    return mark_safe(text)
