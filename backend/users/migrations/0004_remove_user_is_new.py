# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-01-26 10:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180126_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_new',
        ),
    ]