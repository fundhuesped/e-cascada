# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-27 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hc_practicas', '0017_auto_20160926_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='turno',
            name='informed',
            field=models.BooleanField(default=False),
        ),
    ]
