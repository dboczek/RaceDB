# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-04-04 00:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_auto_20170328_1011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='updatelog',
            options={'ordering': ['-created'], 'verbose_name': 'UpdateLog', 'verbose_name_plural': 'UpdateLog'},
        ),
        migrations.AddField(
            model_name='team',
            name='contact',
            field=models.CharField(blank=True, default=b'', max_length=64, verbose_name='Contact'),
        ),
        migrations.AddField(
            model_name='team',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Contact Email'),
        ),
        migrations.AddField(
            model_name='team',
            name='contact_phone',
            field=models.CharField(blank=True, default=b'', max_length=22, verbose_name='Contact Phone'),
        ),
    ]
