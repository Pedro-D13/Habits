# Generated by Django 3.0.2 on 2020-02-21 22:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_auto_20200220_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tdl',
            name='duedate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 22, 18, 0)),
        ),
        migrations.AlterField(
            model_name='tdl',
            name='heading',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todolist.TDLheading'),
        ),
    ]
