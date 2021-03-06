# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-05-06 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0059_customcategorymassstart_customcategorytt'),
    ]

    operations = [
        migrations.AddField(
            model_name='customcategorymassstart',
            name='license_code_prefixes',
            field=models.CharField(blank=True, default=b'', help_text='e.g. "ON,BC" comma separated', max_length=32, verbose_name='License Code Prefixes'),
        ),
        migrations.AddField(
            model_name='customcategorymassstart',
            name='state_prov_str',
            field=models.CharField(blank=True, default=b'', help_text='States or Provinces, comma separated', max_length=128, verbose_name='State/Provs'),
        ),
        migrations.AddField(
            model_name='customcategorytt',
            name='license_code_prefixes',
            field=models.CharField(blank=True, default=b'', help_text='e.g. "ON,BC" comma separated', max_length=32, verbose_name='License Code Prefixes'),
        ),
        migrations.AddField(
            model_name='customcategorytt',
            name='state_prov_str',
            field=models.CharField(blank=True, default=b'', help_text='States or Provinces, comma separated', max_length=128, verbose_name='State/Provs'),
        ),
        migrations.AlterField(
            model_name='customcategorymassstart',
            name='date_of_birth_maximum',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Date of Birth <='),
        ),
        migrations.AlterField(
            model_name='customcategorymassstart',
            name='date_of_birth_minimum',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Date of Birth >='),
        ),
        migrations.AlterField(
            model_name='customcategorytt',
            name='date_of_birth_maximum',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Date of Birth <='),
        ),
        migrations.AlterField(
            model_name='customcategorytt',
            name='date_of_birth_minimum',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Date of Birth >='),
        ),
    ]
