# Generated by Django 2.0.4 on 2018-05-14 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20180506_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='executor',
            name='task',
        ),
        migrations.DeleteModel(
            name='Executor',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]