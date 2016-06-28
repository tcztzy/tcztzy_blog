from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.active().filter(pub_date__lte=timezone.now())

    def active(self):
        return self.filter(is_active=True)


class Entry(models.Model):
    headline = models.CharField(max_length=200)
    slug = models.SlugField(unique_for_date='pub_date')
    is_active = models.BooleanField(
        help_text=_(
            "Tick to make this entry live (see also the publication date). "
            "Note that administrators (like yourself) are allowed to preview "
            "inactive entries whereas the general public aren't."
        ),
        default=False,
    )
    author = models.CharField(max_length=100)
    pub_date = models.DateTimeField(
        verbose_name=_("Publication date"),
        help_text=_(
            "For an entry to be published, it must be active and its "
            "publication date must be in the past."
        ),
    )
    summary = models.TextField(blank=True, null=True)
    body = models.TextField()

    objects = EntryQuerySet.as_manager()

    class Meta:
        db_table = 'blog_entries'
        verbose_name_plural = 'entries'
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'

    def __str__(self):
        return self.headline

    def is_published(self):
        """
        Return True if the entry is publicly accessible.
        """
        return self.is_active and self.pub_date <= timezone.now()
    is_published.boolean = True

    def save(self, *args, **kwargs):

        super(Entry, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return self.slug
