# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-27 15:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crawl', '0006_input_processed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='input',
            old_name='container_identifier',
            new_name='post_container_identifier',
        ),
        migrations.AddField(
            model_name='input',
            name='category_container_identifier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category_container_identifier', to='crawl.ContentIdentifier'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='input',
            name='post_link_identifier',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='post_link_identifier', to='crawl.ContentIdentifier'),
            preserve_default=False,
        ),
    ]
