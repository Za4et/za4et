# Generated by Django 2.0.4 on 2018-05-04 17:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20180504_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 5, 4, 17, 45, 29, 87522, tzinfo=utc)),
        ),
    ]
