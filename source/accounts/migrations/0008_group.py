# Generated by Django 2.2 on 2020-01-28 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0007_useradminposition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Группа')),
                ('started_at', models.DateField(verbose_name='Дата создания')),
                ('kurator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kurator', to=settings.AUTH_USER_MODEL, verbose_name='Куратор')),
                ('starosta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='starosta', to=settings.AUTH_USER_MODEL, verbose_name='Староста')),
                ('students', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
