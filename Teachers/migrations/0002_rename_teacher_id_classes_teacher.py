# Generated by Django 3.2.13 on 2022-07-03 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teachers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classes',
            old_name='teacher_id',
            new_name='teacher',
        ),
    ]
