# Generated by Django 2.2 on 2020-01-30 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_remove_saturdaylesson_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='name',
        ),
        migrations.AlterField(
            model_name='saturdaylesson',
            name='index',
            field=models.IntegerField(verbose_name='Порядковый номер'),
        ),
    ]
