# Generated by Django 5.1.4 on 2025-01-27 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_task_is_complete_alter_task_task_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]
