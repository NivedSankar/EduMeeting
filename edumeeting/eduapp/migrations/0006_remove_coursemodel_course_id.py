# Generated by Django 4.2.7 on 2023-11-30 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eduapp', '0005_coursemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursemodel',
            name='course_id',
        ),
    ]
