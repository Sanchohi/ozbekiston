# Generated by Django 4.0.4 on 2022-05-17 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viloyat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rayon',
            name='img',
        ),
    ]