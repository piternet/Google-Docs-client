# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-09 09:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('googledocs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='creation_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
