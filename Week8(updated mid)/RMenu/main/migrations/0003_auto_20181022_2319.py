# Generated by Django 2.1.2 on 2018-10-22 17:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20181022_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishreview',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 22, 23, 19, 42, 881914)),
        ),
        migrations.AlterField(
            model_name='restrewiew',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 22, 23, 19, 42, 881477)),
        ),
    ]
