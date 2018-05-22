# Generated by Django 2.0.4 on 2018-04-21 15:48

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20180420_2114'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discipline',
            options={'verbose_name': 'Дисциплину', 'verbose_name_plural': 'Дисциплины'},
        ),
        migrations.AlterModelOptions(
            name='tagfiles',
            options={'verbose_name': 'Категорию файлов', 'verbose_name_plural': 'Категории файлов'},
        ),
        migrations.AlterField(
            model_name='files',
            name='discipline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Discipline', verbose_name='Дисциплина'),
        ),
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(upload_to=main.models.file_upload_to, verbose_name='Прикрепить материал'),
        ),
    ]
