# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-26 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_personinfo_is_spam'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='average_expression',
            field=models.FloatField(default=5.0),
        ),
        migrations.AddField(
            model_name='assessment',
            name='average_interesting',
            field=models.FloatField(default=5.0),
        ),
        migrations.AddField(
            model_name='assessment',
            name='expression_ability',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='assessment',
            name='interesting',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='cooperation_rate',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='general_rate',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='profession_rate',
            field=models.IntegerField(default=5),
        ),
    ]
