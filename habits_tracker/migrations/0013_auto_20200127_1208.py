# Generated by Django 3.0.2 on 2020-01-27 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habits_tracker', '0012_auto_20200127_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    primary_key=True, serialize=False, to='habits_tracker.Person'),
        ),
        migrations.RemoveField(
            model_name='habit',
            name='goal',
        ),
        migrations.AddField(
            model_name='habit',
            name='goal',
            field=models.ForeignKey(
                default=2, on_delete=django.db.models.deletion.CASCADE, to='habits_tracker.Goal'),
            preserve_default=False,
        ),
    ]
