# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-27 20:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hc_common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hc_common.Persona')),
                ('idpaciente', models.CharField(max_length=20, null=True)),
                ('prospect', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('hc_common.persona',),
        ),
    ]
