# Generated by Django 4.0.5 on 2022-07-09 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='titile',
            new_name='title',
        ),
    ]
