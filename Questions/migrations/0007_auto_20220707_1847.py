# Generated by Django 3.2.13 on 2022-07-07 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0006_rename_ques_detail_questionbankdesc_ques_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionbankdesc',
            name='ques_answer',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='questionbankdesc',
            name='ques_sample',
            field=models.CharField(max_length=255),
        ),
    ]
