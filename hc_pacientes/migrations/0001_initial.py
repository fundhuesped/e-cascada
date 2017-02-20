# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-30 22:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hc_common', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hc_common.Persona')),
                ('idpaciente', models.CharField(max_length=20, null=True)),
                ('prospect', models.BooleanField(default=False)),
                ('consent', models.CharField(choices=[(b'Yes', b'Si'), (b'No', b'No'), (b'Not asked', b'No preguntado')], default=b'Not asked', max_length=14)),
                ('updated_on', models.DateField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('hc_common.persona',),
        ),
    ]
