from django.conf.urls import url
from blog.views import (BlogArchiveIndexView, BlogYearArchiveView,
                        BlogMonthArchiveView, BlogDayArchiveView,
                        BlogDateDetailView)

app_name = 'blog'
urlpatterns = [
    url(
        r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[\w-]+)/$',
        BlogDateDetailView.as_view(),
        name="entry"
    ),
    url(
        r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$',
        BlogDayArchiveView.as_view(),
        name="archive-day"
    ),
    url(
        r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$',
        BlogMonthArchiveView.as_view(),
        name="archive-month"
    ),
    url(
        r'^(?P<year>\d{4})/$',
        BlogYearArchiveView.as_view(),
        name="archive-year"
    ),
    url(
        r'^$',
        BlogArchiveIndexView.as_view(),
        name="index"
    ),
]
