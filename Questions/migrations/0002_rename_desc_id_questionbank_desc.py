# Generated by Django 3.2.13 on 2022-07-03 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionbank',
            old_name='desc_id',
            new_name='desc',
        ),
    ]
