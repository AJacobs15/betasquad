# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 14:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Players',
        ),
    ]
