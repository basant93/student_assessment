# Generated by Django 2.1 on 2019-01-03 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuestionBank', '0002_auto_20190103_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionbanks',
            name='total_time',
            field=models.TimeField(blank=True),
        ),
    ]
