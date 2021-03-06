# Generated by Django 3.2.4 on 2022-02-19 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('task_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('task_description', models.TextField()),
                ('task_completed', models.BooleanField(default=False)),
                ('task_created', models.DateTimeField(auto_now_add=True)),
                ('task_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
