# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 05:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawl', '0002_auto_20161126_1734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='input',
            old_name='post_container_identifiers',
            new_name='container_identifiers',
        ),
    ]
