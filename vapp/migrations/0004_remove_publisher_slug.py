# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 13:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vapp', '0003_publisher_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='slug',
        ),
    ]
