# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-27 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]
