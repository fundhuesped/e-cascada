# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2019-03-29 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hc_pacientes', '0002_auto_20190329_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='idpaciente',
            field=models.CharField(max_length=20, null=True),
        ),
    ]