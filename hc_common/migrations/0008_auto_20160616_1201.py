# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-16 15:01
from __future__ import unicode_literals

from django.db import migrations


def loadDistrict(apps, schema_editor):
    Province = apps.get_model("hc_common", "Province")
    District = apps.get_model("hc_common", "District")

    District(
        name="No informa",
        description="No informa",
        status="Active",
        province=Province.objects.get(name="No informa")
        ).save()

    District(
        name="CABA",
        description="Ciudad Autónoma de Buenos Aires",
        status="Active",
        province=Province.objects.get(name="CABA")
        ).save()


class Migration(migrations.Migration):

    dependencies = [
        ('hc_common', '0007_auto_20160616_1141'),
    ]

    operations = [
        migrations.RunPython(loadDistrict),
    ]