from django import template

register = template.Library()


class EligibleNode(template.Node):
    def __init__(self, varname=None, user=None):
        if user is None:
            raise template.TemplateSyntaxError('Eligible template nodes must be given a user to return.')
        self.user = user
        self.varname = varname

    def render(self, context):
        user = self.user.resolve(context)
        if self.varname is None:
            return user.is_eligible()
        context[self.varname] = user.is_eligible()
        return ''

    @classmethod
    def handle_token(cls, parser, token):
        """
        Class method to parse prefix node and return a Node.
        """
        bits = token.split_contents()

        if len(bits) < 2:
            raise template.TemplateSyntaxError("'%s' takes at least one argument (user)" % bits[0])

        user = parser.compile_filter(bits[1])

        if len(bits) >= 2 and bits[-2] == 'as':
            varname = bits[3]
        else:
            varname = None

        return cls(varname, user)


@register.tag
def eligible(parser, token):
    """
    Displays "allowed" if the user is older than 13 years otherwise display
    "blocked".

    Usage::

        {% eligible user [as varname] %}

    Examples::

        {% eligible variable_with_user %}
        {% eligible variable_with_user as varname %}
    """
    return EligibleNode.handle_token(parser, token)


@register.tag
def bizzfuzz(parser, token):
    pass
