# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-19 15:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hc_practicas', '0015_auto_20160902_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='TurnoSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('start', models.TimeField(default=b'08:00:00')),
                ('end', models.TimeField(default=b'17:00:00')),
                ('status', models.CharField(choices=[(b'Active', b'Activo'), (b'Inactive', b'Inactivo')], default=b'Active', max_length=8)),
                ('state', models.CharField(choices=[(b'Available', b'Disponible'), (b'Occupied', b'Ocupado'), (b'Conflict', b'En conflicto'), (b'Deleted', b'Eliminado')], max_length=10)),
                ('updated_on', models.DateField(auto_now=True)),
                ('agenda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hc_practicas.Agenda')),
                ('prestacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hc_practicas.Prestacion')),
                ('profesional', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hc_practicas.Profesional')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='turno',
            name='agenda',
        ),
        migrations.RemoveField(
            model_name='turno',
            name='day',
        ),
        migrations.RemoveField(
            model_name='turno',
            name='end',
        ),
        migrations.RemoveField(
            model_name='turno',
            name='prestacion',
        ),
        migrations.RemoveField(
            model_name='turno',
            name='profesional',
        ),
        migrations.RemoveField(
            model_name='turno',
            name='start',
        ),
        migrations.RemoveField(
            model_name='turno',
            name='taken',
        ),
        migrations.AddField(
            model_name='turno',
            name='notes',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='turno',
            name='state',
            field=models.CharField(choices=[(b'Initial', b'Inicial'), (b'Present', b'Presente'), (b'Absent', b'Ausente'), (b'Served', b'Atendido'), (b'Canceled', b'Cancelado')], default='Initial', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='turno',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hc_pacientes.Paciente'),
        ),
        migrations.AddField(
            model_name='turno',
            name='turnoSlot',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hc_practicas.TurnoSlot'),
            preserve_default=False,
        ),
    ]