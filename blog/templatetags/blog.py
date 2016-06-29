from django import template

from ..models import Entry

register = template.Library()


@register.inclusion_tag('includes/about.html')
def about_this_blog():
    return {}


@register.inclusion_tag('blog/month_links_snippet.html')
def render_month_links():
    return {
        'dates': Entry.objects.published().datetimes('pub_date', 'month', order='DESC')
    }
