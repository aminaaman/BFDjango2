# Generated by Django 2.1.2 on 2018-10-31 19:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20181031_1902'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='comment',
            name='cr_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 31, 19, 8, 17, 633834)),
        ),
        migrations.AlterField(
            model_name='post',
            name='cr_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 31, 19, 8, 17, 633402)),
        ),
    ]
