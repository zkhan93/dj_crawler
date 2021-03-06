# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 12:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crawl', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='input',
            name='content_identifiers',
        ),
        migrations.AddField(
            model_name='input',
            name='category_name_identifier',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='category_name_identifier', to='crawl.ContentIdentifier'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='input',
            name='category_summary_identifier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category_summary_identifier', to='crawl.ContentIdentifier'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='input',
            name='category_title_identifier',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='category_title_identifier', to='crawl.ContentIdentifier'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='input',
            name='post_container_identifiers',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='post_container_identifier', to='crawl.ContentIdentifier'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='input',
            name='post_summary_identifiers',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='post_summary_identifier', to='crawl.ContentIdentifier'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='input',
            name='post_title_identifiers',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='post_title_identifier', to='crawl.ContentIdentifier'),
            preserve_default=False,
        ),
    ]
