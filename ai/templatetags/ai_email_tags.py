#from https://djangosnippets.org/snippets/10482/
from django import template

register = template.Library()

class ObfuscateEmail(template.Node):
    def __init__(self, email, link_body=None):
        self.email = template.Variable(email)

        try:
            self.link_body = template.Variable(link_body)
        except (template.VariableDoesNotExist, TypeError):
            self.link_body = None

    def render(self, context):
        import random
        email_address = str(self.email)
        character_set = '+-.0123456789@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz'
        char_list = list(character_set)
        random.shuffle(char_list)

        key = ''.join(char_list)

        cipher_text = ''
        id = 'e' + str(random.randrange(1,999999999))

        for a in email_address:
            cipher_text += key[ character_set.find(a) ]

        script = 'var a="{}";var b=a.split("").sort().join("");var c="{}";var d="";' \
                 'for(var e=0;e<c.length;e++)d+=b.charAt(a.indexOf(c.charAt(e)));' \
                 'document.getElementById("{}").innerHTML="<a href=\\"mailto:"+d+"\\">"+{}+"</a>"'.format(key, cipher_text, id, self.link_body or 'd')

        script = "eval(\""+ script.replace("\\","\\\\").replace('"','\\"') + "\")"
        script = '<script type="text/javascript">/*<![CDATA[*/'+script+'/*]]>*/</script>'

        return '<span id="{}">[javascript protected email address]</span>{}'.format(id, script)


@register.tag
def obfuscate_email(parser, token):
    """
        {% obfuscate_email user.email %}
    """

    bits = token.split_contents()
    """
    Pass all of the arguments defined in the template tag except the first one,
    which will be the name of the template tag itself.
    Example: {% do_whatever arg1 arg2 arg3 %}
    *bits[1:] would be: [arg1, arg2, arg3]
    """

    if len(bits) not in (2, 3):
        raise template.TemplateSyntaxError("{} accepts one or two arguments: 1) (required) email 2) (optional) <a> tag body ")

    return ObfuscateEmail(*bits[1:])