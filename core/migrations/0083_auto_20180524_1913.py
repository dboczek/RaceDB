# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2018-05-24 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0082_licensecheckstate_discipline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(db_index=True, max_length=128, verbose_name='Name'),
        ),
    ]
