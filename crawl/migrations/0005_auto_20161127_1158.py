# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 06:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawl', '0004_auto_20161127_1050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='input',
            old_name='container_identifiers',
            new_name='container_identifier',
        ),
        migrations.RenameField(
            model_name='input',
            old_name='post_summary_identifiers',
            new_name='post_summary_identifier',
        ),
        migrations.RenameField(
            model_name='input',
            old_name='post_title_identifiers',
            new_name='post_title_identifier',
        ),
    ]
