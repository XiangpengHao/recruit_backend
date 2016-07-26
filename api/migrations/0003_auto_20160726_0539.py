# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-26 05:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20160725_0740'),
    ]

    operations = [
        migrations.AddField(
            model_name='personinfo',
            name='is_spam',
            field=models.TextField(default='false', max_length=100),
        ),
        migrations.AddField(
            model_name='personinfo',
            name='time_spend',
            field=models.TextField(default='not given', max_length=100),
        ),
        migrations.AddField(
            model_name='personinfo',
            name='user_agent',
            field=models.TextField(default='not given', max_length=1000),
        ),
    ]
