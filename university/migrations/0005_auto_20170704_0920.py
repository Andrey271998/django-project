# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0004_auto_20170703_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evalution',
            name='appraisal',
            field=models.CharField(max_length=3, verbose_name=b'\xd0\x9e\xd1\x86\xd0\xb5\xd0\xbd\xd0\xba\xd0\xb0'),
        ),
    ]
