# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-07 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0006_auto_20170707_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='evalution',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]