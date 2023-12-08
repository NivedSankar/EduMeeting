# Generated by Django 4.2.7 on 2023-11-14 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduapp', '0003_studentreg_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('qualification', models.CharField(max_length=500)),
                ('photo', models.FileField(upload_to='eduapp/static/assets/images')),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]