# Generated by Django 2.2 on 2020-01-30 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_lesson_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='saturdaylesson',
            name='index',
            field=models.IntegerField(default=1, verbose_name='Порядковый номер'),
        ),
    ]