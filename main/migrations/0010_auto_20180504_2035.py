# Generated by Django 2.0.4 on 2018-05-04 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20180429_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Executor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('1', 'open'), ('2', 'closed')], max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
        migrations.AlterField(
            model_name='journal',
            name='link',
            field=models.URLField(help_text='Скопируйте ссылку и вставьте в это поле.Не забудьте предоставить доступ к таблице.', verbose_name='Ссылка на журнал'),
        ),
        migrations.AddField(
            model_name='executor',
            name='task',
            field=models.ManyToManyField(to='main.Task'),
        ),
    ]
