# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-23 10:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='student',
            new_name='Students',
        ),
    ]
