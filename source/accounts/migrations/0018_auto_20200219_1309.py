# Generated by Django 2.2 on 2020-02-19 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20200219_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studygroup',
            name='group_leader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leader', to=settings.AUTH_USER_MODEL, verbose_name='Староста'),
        ),
    ]