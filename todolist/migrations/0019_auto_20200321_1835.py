# Generated by Django 3.0.4 on 2020-03-21 18:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0018_auto_20200311_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tditem',
            name='duedate',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 22, 18, 0, tzinfo=utc)),
        ),
    ]
