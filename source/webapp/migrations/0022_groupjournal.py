# Generated by Django 2.2 on 2020-02-26 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20200219_1310'),
        ('webapp', '0021_auto_20200217_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupJournal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journal_discipline', to='webapp.Discipline', verbose_name='Дисциплина')),
                ('study_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journal_group', to='accounts.StudyGroup', verbose_name='Группа')),
            ],
        ),
    ]