# Generated by Django 3.2.4 on 2022-01-04 14:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_auto_20220104_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_task',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 4, 14, 52, 39, 48313, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='my_task',
            name='deadline',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 4, 14, 52, 39, 110804, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='my_task',
            name='remainder_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 4, 14, 52, 39, 110804, tzinfo=utc), help_text='add date only if remainder type is custom', null=True),
        ),
        migrations.AlterField(
            model_name='my_task',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2022, 1, 4, 14, 52, 39, 110804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='my_task',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2022, 1, 4, 14, 52, 39, 110804, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='my_task',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2022, 1, 4, 14, 52, 39, 110804, tzinfo=utc)),
        ),
    ]
