# Generated by Django 4.2.7 on 2023-11-10 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentreg',
            name='photo',
            field=models.FileField(default=1, upload_to='eduapp/static/assets/images'),
            preserve_default=False,
        ),
    ]