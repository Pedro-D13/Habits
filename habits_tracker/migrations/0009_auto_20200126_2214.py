# Generated by Django 3.0.2 on 2020-01-26 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits_tracker', '0008_auto_20200126_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='goal',
            field=models.ManyToManyField(to='habits_tracker.Goal'),
        ),
    ]
