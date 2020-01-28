# Generated by Django 2.2 on 2020-01-24 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_merge_20200124_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passport',
            name='citizenship',
            field=models.CharField(default='Кыргызская Республика', max_length=30, verbose_name='Гражданство'),
        ),
        migrations.AlterField(
            model_name='passport',
            name='sex',
            field=models.CharField(choices=[('мужской', 'мужской'), ('женский', 'женский')], max_length=15, verbose_name='Пол'),
        ),
    ]