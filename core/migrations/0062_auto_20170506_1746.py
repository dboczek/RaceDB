# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-05-06 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0061_auto_20170506_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customcategorymassstart',
            name='date_of_birth_maximum',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Born Before'),
        ),
        migrations.AlterField(
            model_name='customcategorymassstart',
            name='date_of_birth_minimum',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Born After'),
        ),
        migrations.AlterField(
            model_name='customcategorymassstart',
            name='nation_code_str',
            field=models.CharField(blank=True, default=b'', help_text='3-letter IOC Country Codes, comma separated', max_length=128, verbose_name='Nation Codes'),
        ),
        migrations.AlterField(
            model_name='customcategorytt',
            name='date_of_birth_maximum',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Born Before'),
        ),
        migrations.AlterField(
            model_name='customcategorytt',
            name='date_of_birth_minimum',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Born After'),
        ),
    ]
