# Generated by Django 3.2.14 on 2022-07-09 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0008_auto_20220709_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionbankdesc',
            name='ques_case',
            field=models.CharField(max_length=255),
        ),
    ]