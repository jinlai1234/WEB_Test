# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-27 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seven', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icon',
            name='ico',
            field=models.ImageField(upload_to='%Y/%m/%d/img'),
        ),
    ]
