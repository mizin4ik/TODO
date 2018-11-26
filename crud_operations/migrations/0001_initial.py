# Generated by Django 2.1.3 on 2018-11-26 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=256)),
                ('start_task', models.DateField()),
                ('deadline', models.DateField()),
                ('todo', models.BooleanField(default=False)),
                ('in_progress', models.BooleanField(default=False)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
