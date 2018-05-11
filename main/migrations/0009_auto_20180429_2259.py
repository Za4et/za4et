# Generated by Django 2.0.4 on 2018-04-29 19:59

import autoslug.fields
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('main', '0008_auto_20180421_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormStyding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Форма обучения')),
            ],
            options={
                'verbose_name': 'Форма обучения',
                'verbose_name_plural': 'Формы обучения',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('form_edu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.FormStyding', verbose_name='Форма обучения')),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Institute', verbose_name='Институт')),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(help_text='Скопируйте ссылку и вставьте в это поле', verbose_name='Ссылка на журнал')),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Discipline', verbose_name='Предмет')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Group', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Журнал',
                'verbose_name_plural': 'Журналы',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('fio', models.CharField(max_length=400, verbose_name='Ф.И.О студента')),
                ('place_of_styding', models.TextField(verbose_name='Место обучения студента')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=main.models.avatar_upload)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Group', verbose_name='Учебная группа')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.news_upload_to, verbose_name='Изображение к новости'),
        ),
    ]
