# Generated by Django 2.2 on 2020-02-14 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20200214_1144'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserAdminPosition',
        ),
    ]