# Generated by Django 3.0.2 on 2020-02-08 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_title', models.CharField(max_length=25)),
                ('goal_status', models.CharField(choices=[('TS', 'To start'), ('PR', 'progressing'), ('AC', 'Achieved')], max_length=20)),
                ('mantra', models.TextField()),
            ],
        ),
    ]
