# Generated by Django 3.2.7 on 2022-08-07 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_raise_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketraise',
            name='assigned_to',
        ),
    ]
