# Generated by Django 2.2.1 on 2019-05-29 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todoitem',
            name='date_created',
        ),
    ]
