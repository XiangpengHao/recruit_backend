# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-01 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20160829_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='personinfo',
            name='mail_address',
            field=models.TextField(default=''),
        ),
    ]