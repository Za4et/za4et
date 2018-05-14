# -*- coding: utf-8 -*-
import os
import random
import sys

from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


def news_upload_to(instance, filename):
    rand = random.randrange(0, sys.maxsize)
    rand = str(rand)
    return os.path.join('news_imgs/', rand + os.path.splitext(filename)[1])


def file_upload_to(instance, filename):
    rand = random.randrange(0, sys.maxsize)
    rand = str(rand)
    return os.path.join('materials/', rand + os.path.splitext(filename)[1])


def avatar_upload(instance, filename):
    rand = random.randrange(0, sys.maxsize)
    rand = str(rand)
    return os.path.join('avatars/', rand + os.path.splitext(filename)[1])


class Discipline(models.Model):
    class Meta:
        verbose_name = 'Дисциплину'
        verbose_name_plural = 'Дисциплины'

    name = models.CharField(max_length=200, verbose_name='Дисциплина')
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name


class TagFiles(models.Model):
    class Meta:
        verbose_name = 'Категорию файлов'
        verbose_name_plural = 'Категории файлов'

    name = models.CharField(max_length=200, verbose_name='Категория')
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name


class Teacher(models.Model):
    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    fio = models.CharField(max_length=200, verbose_name='Преподаватель')

    def __str__(self):
        return self.fio


class Files(models.Model):
    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'

    name = models.CharField(max_length=400, verbose_name='Название файла')
    file = models.FileField(upload_to=file_upload_to, verbose_name='Прикрепить материал', name='file')
    teacher = models.ForeignKey(Teacher, verbose_name='Преподаватель', on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name='Дисциплина', null=True,
                                   blank=True)
    tag = models.ManyToManyField(TagFiles, verbose_name='Категории', null=True, blank=True)

    def __str__(self):
        return self.name


class Institute(models.Model):
    class Meta:
        verbose_name = 'Институт'
        verbose_name_plural = 'Институты'

    name = models.CharField(max_length=300, verbose_name='Название института', blank=True, null=True)
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name + '\n'


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории новостей'

    title = models.CharField(max_length=300, blank=True, null=True)
    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return self.title


class News(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published']

    title = models.CharField(max_length=500, blank=True, null=True, verbose_name='Заголовок')
    text = RichTextField(verbose_name='Текст новости')
    file = models.FileField(verbose_name='Прикрепить документ', blank=True, null=True, upload_to='news/')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ManyToManyField(Category, verbose_name='Категории',
                                      help_text='Зажмите Ctrl , чтоб выбрать несколько категорий.'
                                      )
    image = models.ImageField(verbose_name='Изображение к новости', blank=True, null=True, upload_to=news_upload_to)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    published = models.DateTimeField(default=timezone.now, verbose_name='Опубликовано')
    slug = AutoSlugField(populate_from='title')
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Институт')

    def __str__(self):
        return str(self.title)

    def short_text(self):
        return self.text[7:200] + '...'

    def get_absolute_url(self):
        year = str(self.published.year)
        month = str(self.published.strftime('%m'))
        day = str(self.published.strftime('%d'))
        slug = str(self.slug)
        returned = '/news' + '/' + year + '/' + month + '/' + day + '/' + slug + '/'
        return returned


class FormStyding(models.Model):
    class Meta:
        verbose_name = "Форма обучения"
        verbose_name_plural = 'Формы обучения'

    name = models.CharField(max_length=300, verbose_name='Форма обучения')

    def __str__(self):
        return self.name


class Group(models.Model):
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name')
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, verbose_name='Институт')
    form_edu = models.ForeignKey(FormStyding, on_delete=models.CASCADE, verbose_name='Форма обучения')
    cource = models.PositiveIntegerField(verbose_name='Курс')

    def __str__(self):
        return self.name


class Student(User):
    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    fio = models.CharField(max_length=400, verbose_name='Ф.И.О студента'
                           )
    place_of_styding = models.TextField(verbose_name='Место обучения студента')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Учебная группа')
    avatar = models.ImageField(upload_to=avatar_upload, blank=True, null=True)

    def __str__(self):
        return self.fio


class Journal(models.Model):
    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'

    link = models.URLField(verbose_name='Ссылка на журнал', help_text='Скопируйте ссылку и вставьте в это поле.'
                                                                      'Не забудьте предоставить доступ к таблице.')

    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name='Предмет')

    def __str__(self):
        return self.link


class Task(models.Model):
    task = models.CharField(max_length=200)
    status = models.CharField(choices=[('1', 'open'), ('2', 'closed')], max_length=200)
    date = models.DateField(default=timezone.now)


class Executor(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
