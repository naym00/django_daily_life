# Generated by Django 5.1.4 on 2024-12-25 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
