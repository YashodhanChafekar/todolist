# Generated by Django 4.0.1 on 2022-07-08 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='meetlink',
            field=models.URLField(blank=True, null=True),
        ),
    ]