# Generated by Django 3.0.2 on 2020-03-03 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0011_auto_20200303_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tdlsubtitle',
            name='item',
        ),
        migrations.DeleteModel(
            name='TDLnotes',
        ),
        migrations.DeleteModel(
            name='TDLsubtitle',
        ),
    ]