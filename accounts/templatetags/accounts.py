from django import template

register = template.Library()


@register.tag
def is_allowed(parser, token):
    pass


@register.tag
def bizz_fuzz(parser, token):
    pass
