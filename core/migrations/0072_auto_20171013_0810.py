# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-10-13 12:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0071_auto_20170718_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamhint',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Team'),
        ),
    ]
