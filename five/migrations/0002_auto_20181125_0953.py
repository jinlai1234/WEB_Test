# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-25 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('five', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idcard',
            name='id_num',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]
