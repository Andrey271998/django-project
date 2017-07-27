# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 09:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.IntegerField(default=0, verbose_name=b'\xd0\x9a\xd1\x83\xd1\x80\xd1\x81')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.CharField(max_length=255, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xba\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb5\xd1\x82')),
            ],
        ),
        migrations.CreateModel(
            name='Evalution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appraisal', models.IntegerField(default=0, verbose_name=b'\xd0\x9e\xd1\x86\xd0\xb5\xd0\xbd\xd0\xba\xd0\xb0')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party', models.CharField(max_length=255, verbose_name=b'\xd0\x93\xd1\x80\xd1\x83\xd0\xbf\xd0\xb0')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f')),
                ('surname', models.CharField(max_length=255, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('cource', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='university.Cource', verbose_name=b'\xd0\x9a\xd1\x83\xd1\x80\xd1\x81')),
                ('department', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='university.Department', verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xba\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb5\xd1\x82')),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='university.Group', verbose_name=b'\xd0\x93\xd1\x80\xd1\x83\xd0\xbf\xd0\xb0')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matter', models.CharField(max_length=255, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb4\xd0\xbc\xd0\xb5\xd1\x82')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f')),
                ('surname', models.CharField(max_length=255, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f')),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.Teacher'),
        ),
        migrations.AddField(
            model_name='group',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.Teacher'),
        ),
        migrations.AddField(
            model_name='evalution',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.Students', verbose_name=b'\xd0\xa1\xd1\x82\xd1\x83\xd0\xb4\xd0\xb5\xd0\xbd\xd1\x82'),
        ),
        migrations.AddField(
            model_name='evalution',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.Subject', verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb4\xd0\xbc\xd0\xb5\xd1\x82'),
        ),
        migrations.AddField(
            model_name='evalution',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.Teacher', verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb5\xd0\xbf\xd0\xbe\xd0\xb4\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c'),
        ),
        migrations.AddField(
            model_name='department',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.Teacher'),
        ),
    ]
