# Generated by Django 2.0.4 on 2018-05-06 14:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20180504_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='cource',
            field=models.PositiveIntegerField(default=1, verbose_name='Курс'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 5, 6, 14, 25, 55, 662261, tzinfo=utc)),
        ),
    ]