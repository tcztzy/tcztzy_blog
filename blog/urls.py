from django.conf.urls import url
from blog.views import BlogArchiveIndexView

urlpatterns = [
    url('^$', BlogArchiveIndexView.as_view(), name='None'),
]
