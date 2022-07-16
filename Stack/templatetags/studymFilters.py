from django import template

register = template.Library()

@register.simple_tag
def boldSearchedQ(value, q):
    return value.replace(q, f"<b>{q}</b>")