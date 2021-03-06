# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-01-07 13:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_systeminfo_cloud_server_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.PositiveSmallIntegerField(blank=True, default=32767, verbose_name='Sequence')),
                ('name', models.CharField(default=b'MyGroup', max_length=32, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'CategoryGroup',
                'verbose_name_plural': 'CategoryGroups',
            },
        ),
        migrations.CreateModel(
            name='CategoryGroupElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category')),
                ('category_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CategoryGroup')),
            ],
            options={
                'ordering': ['category__sequence'],
                'verbose_name': 'CategoryGroupElement',
                'verbose_name_plural': 'CategoryGroupElements',
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.PositiveSmallIntegerField(blank=True, default=32767, verbose_name='Sequence')),
                ('name', models.CharField(default=b'MySeries', max_length=32, verbose_name='Name')),
                ('description', models.CharField(blank=True, default=b'', max_length=80, verbose_name='Description')),
                ('tie_breaking_rule', models.PositiveSmallIntegerField(choices=[(5, 'Number of 1st, 2nd, 3rd, 4th then 5th place finishes'), (4, 'Number of 1st, 2nd, 3rd then 4th place finishes'), (3, 'Number of 1st, 2nd then 3rd place finishes'), (2, 'Number of 1st then 2nd place finishes'), (1, 'Number of 1st place finishes'), (0, 'Do not consider place finishes')], default=5, verbose_name='Tie-breaking Rule')),
                ('best_results_to_consider', models.PositiveSmallIntegerField(choices=[(0, 'All Results'), (1, 'Best Result Only'), (2, '2 Best Results Only'), (3, '3 Best Results Only'), (4, '4 Best Results Only'), (5, '5 Best Results Only'), (6, '6 Best Results Only'), (7, '7 Best Results Only'), (8, '8 Best Results Only'), (9, '9 Best Results Only'), (10, '10 Best Results Only'), (11, '11 Best Results Only'), (12, '12 Best Results Only'), (13, '13 Best Results Only'), (14, '14 Best Results Only'), (15, '15 Best Results Only'), (16, '16 Best Results Only'), (17, '17 Best Results Only'), (18, '18 Best Results Only'), (19, '19 Best Results Only'), (20, '20 Best Results Only'), (21, '21 Best Results Only'), (22, '22 Best Results Only'), (23, '23 Best Results Only'), (24, '24 Best Results Only'), (25, '25 Best Results Only'), (26, '26 Best Results Only'), (27, '27 Best Results Only'), (28, '28 Best Results Only'), (29, '29 Best Results Only'), (30, '30 Best Results Only')], default=0, verbose_name='Consider')),
                ('must_have_completed', models.PositiveSmallIntegerField(choices=[(0, 'All Results'), (1, 'Best Result Only'), (2, '2 Best Results Only'), (3, '3 Best Results Only'), (4, '4 Best Results Only'), (5, '5 Best Results Only'), (6, '6 Best Results Only'), (7, '7 Best Results Only'), (8, '8 Best Results Only'), (9, '9 Best Results Only'), (10, '10 Best Results Only'), (11, '11 Best Results Only'), (12, '12 Best Results Only'), (13, '13 Best Results Only'), (14, '14 Best Results Only'), (15, '15 Best Results Only'), (16, '16 Best Results Only'), (17, '17 Best Results Only'), (18, '18 Best Results Only'), (19, '19 Best Results Only'), (20, '20 Best Results Only'), (21, '21 Best Results Only'), (22, '22 Best Results Only'), (23, '23 Best Results Only'), (24, '24 Best Results Only'), (25, '25 Best Results Only'), (26, '26 Best Results Only'), (27, '27 Best Results Only'), (28, '28 Best Results Only'), (29, '29 Best Results Only'), (30, '30 Best Results Only')], default=0, verbose_name='Must have completed')),
                ('ranking_criteria', models.PositiveSmallIntegerField(choices=[(0, 'Points'), (1, 'Time'), (2, '% Finish/Winning Time')], default=0, verbose_name='Ranking Criteria')),
                ('category_format', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CategoryFormat')),
            ],
            options={
                'ordering': ['sequence'],
                'verbose_name': 'Series',
                'verbose_name_plural': 'Series',
            },
        ),
        migrations.CreateModel(
            name='SeriesCompetitionEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_mass_start', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.EventMassStart')),
                ('event_tt', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.EventTT')),
            ],
            options={
                'verbose_name': 'SeriesCompetitionEvent',
                'verbose_name_plural': 'SeriesCompetitionEvents',
            },
        ),
        migrations.CreateModel(
            name='SeriesIncludeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Series')),
            ],
            options={
                'ordering': ['category__sequence'],
                'verbose_name': 'SeriesIncludeCategory',
                'verbose_name_plural': 'SeriesIncludeCategories',
            },
        ),
        migrations.CreateModel(
            name='SeriesPointsStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.PositiveSmallIntegerField(blank=True, default=32767, verbose_name='Sequence')),
                ('name', models.CharField(default=b'SeriesPoints', max_length=32, verbose_name='Name')),
                ('points_for_place', models.CharField(default=b'30,25,20,15,10,5,3,1,1,1', max_length=512, verbose_name='Points for Place')),
                ('finish_points', models.PositiveSmallIntegerField(default=0, verbose_name='Finish Points')),
                ('dnf_points', models.PositiveSmallIntegerField(default=0, verbose_name='DNF Points')),
                ('dns_points', models.PositiveSmallIntegerField(default=0, verbose_name='DNS Points')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Series')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'PointsStructure',
                'verbose_name_plural': 'PointsStructures',
            },
        ),
        migrations.CreateModel(
            name='SeriesUpgradeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.PositiveSmallIntegerField(blank=True, default=32767, verbose_name='Sequence')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category')),
            ],
            options={
                'verbose_name': 'SeriesUpgradeCategory',
                'verbose_name_plural': 'SeriesUpgradeCategories',
            },
        ),
        migrations.CreateModel(
            name='SeriesUpgradeProgression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', models.PositiveSmallIntegerField(blank=True, default=32767, verbose_name='Sequence')),
                ('factor', models.FloatField(default=0.5, verbose_name='Factor')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Series')),
            ],
            options={
                'verbose_name': 'SeriesUpgradeProgression',
                'verbose_name_plural': 'SeriesUpgradeProgressions',
            },
        ),
        migrations.AddField(
            model_name='seriesupgradecategory',
            name='upgrade_progression',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.SeriesUpgradeProgression'),
        ),
        migrations.AddField(
            model_name='seriescompetitionevent',
            name='points_structure',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.SeriesPointsStructure'),
        ),
        migrations.AddField(
            model_name='seriescompetitionevent',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Series'),
        ),
        migrations.AddField(
            model_name='categorygroup',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Series'),
        ),
    ]
