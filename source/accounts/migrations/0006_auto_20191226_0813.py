# Generated by Django 2.2 on 2019-12-26 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_socialstatus_usersocialstatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersocialstatus',
            name='role',
        ),
        migrations.AddField(
            model_name='usersocialstatus',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='socstatus', to='accounts.SocialStatus', verbose_name='Cтатус'),
            preserve_default=False,
        ),
    ]