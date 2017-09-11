#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    surname = models.CharField(max_length=255, verbose_name='Фамилия')

    def __unicode__(self):
        return '%s %s' % (self.name, self.surname)


class Department(models.Model):
    faculty = models.CharField(max_length=255, verbose_name='Факультет')
    teacher = models.ForeignKey('Teacher', blank=True, null=True)

    def __unicode__(self):
        return self.faculty


class Cource(models.Model):
    path = models.CharField(max_length=1, verbose_name='Курс')

    def __unicode__(self):
        return self.path


class Group(models.Model):
    party = models.CharField(max_length=255, verbose_name='Група')
    teacher = models.ForeignKey('Teacher', blank=True, null=True)

    def __unicode__(self):
        return self.party


class Subject(models.Model):
    matter = models.CharField(max_length=255, verbose_name='Предмет')
    teacher = models.ForeignKey('Teacher', blank=True, null=True)

    def __unicode__(self):
        return self.matter


class Students(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    photo = models.ImageField(blank=True, null=True)
    department = models.ForeignKey('Department', verbose_name='Факультет')
    cource = models.ForeignKey('Cource', verbose_name='Курс')
    group = models.ForeignKey('Group', verbose_name='Група')

    def __unicode__(self):
        return '%s %s' % (self.name, self.surname)


class Evalution(models.Model):
    appraisal = models.IntegerField(default=0, verbose_name='Оценка')
    teacher = models.ForeignKey('Teacher', verbose_name='Преподователь')
    student = models.ForeignKey('Students', verbose_name='Студент')
    subject = models.ForeignKey('Subject', verbose_name='Предмет')
    date = models.DateField()

    def __unicode__(self):
        self.appraisal = str(self.appraisal)
        return self.appraisal