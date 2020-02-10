# Generated by Django 3.0.2 on 2020-02-09 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits_tracker', '0005_auto_20200208_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='goal_status',
            field=models.CharField(choices=[('TS', 'To Start'), ('PR', 'In Progress'), ('AC', 'Achieved')], default='To Start', max_length=20),
        ),
    ]