from django.views.generic import ArchiveIndexView

from blog.models import Entry


class IndexView(ArchiveIndexView):
    template_name = 'index.html'
    model = Entry
    date_field = 'pub_date'
