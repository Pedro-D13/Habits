# Generated by Django 3.0.2 on 2020-02-11 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habits_tracker', '0009_auto_20200209_1234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goal',
            options={'ordering': ['id']},
        ),
    ]
