# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-30 22:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CivilStatusType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('description', models.CharField(max_length=150, null=True)),
                ('status', models.CharField(choices=[(b'Active', b'Activo'), (b'Inactive', b'Inactivo')], default=b'Active', max_length=8)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('description', models.CharField(max_length=150, null=True)),
                ('status', models.CharField(choices=[(b'Active', b'Activo'), (b'Inactive', b'Inactivo')], default=b'Active', max_length=8)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('description', models.CharField(max_length=150, null=True)),
                ('status', models.CharField(choices=[(b'Active', b'Activo'), (b'Inactive', b'Inactivo')], default=b'Active', max_length=8)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EducationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('description', models.CharField(max_length=150, null=True)),
                ('status', models.CharField(choices=[(b'Active', b'Activo'), (b'Inactive', b'Inactivo')], default=b'Active', max_length=8)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('description', models.CharField(max_length=150, null=True)),
                ('status', models.CharField(choices=[(b'Active', b'Activo'), (b'Inactive', b'Inactivo')], default=b'Active', max_length=8)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hc_common.District')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('description', models.CharField(max_length=150, null=True)),
                ('status', models.CharField(choices=[(b'Active', b'Activo'), (b'Inactive', b'Inactivo')], default=b'Active', max_length=8)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SexType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('description', models.CharField(max_length=150, null=True)),
                ('status', models.CharField(choices=[(b'Active', b'Activo'), (b'Inactive', b'Inactivo')], default=b'Active', max_length=8)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SocialService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('description', models.CharField(max_length=150, null=True)),
                ('status', models.CharField(choices=[(b'Active', b'Activo'), (b'Inactive', b'Inactivo')], default=b'Active', max_length=8)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='district',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hc_common.Province'),
        ),
    ]
