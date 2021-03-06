# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-05-28 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique_for_date='pub_date')),
                ('author', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(help_text='For an entry to be published, it must be active and its publication date must be in the past.', verbose_name='Publication date')),
                ('summary', models.TextField()),
                ('body', models.TextField()),
            ],
            options={
                'ordering': ('-pub_date',),
                'verbose_name_plural': 'entries',
                'db_table': 'blog_entries',
                'get_latest_by': 'pub_date',
            },
        ),
    ]
