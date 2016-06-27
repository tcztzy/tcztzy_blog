from django import template

register = template.Library()


@register.inclusion_tag('includes/about.html')
def about_this_blog():
    return {}
