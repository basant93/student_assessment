# Generated by Django 2.1 on 2019-01-02 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolStudents', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user_group',
        ),
    ]
