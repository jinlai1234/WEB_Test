# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-23 15:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_grade', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=32)),
                ('s_grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='two.Grade')),
            ],
        ),
    ]
