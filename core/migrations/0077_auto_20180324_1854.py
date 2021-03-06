# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2018-03-24 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0076_licensecheckstate'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='do_tag_validation',
            field=models.BooleanField(default=True, verbose_name='Do Tag Validation'),
        ),
        migrations.AddField(
            model_name='participant',
            name='tag_checked',
            field=models.BooleanField(default=False, verbose_name='Tag Checked'),
        ),
    ]
