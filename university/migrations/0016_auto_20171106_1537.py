# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-06 15:37
from __future__ import unicode_literals

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0015_auto_20171106_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to=b'photo_student'),
        ),
    ]
