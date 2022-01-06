# Generated by Django 3.2.4 on 2022-01-06 14:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_auto_20220104_2022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='my_task',
            name='club_name',
        ),
        migrations.AlterField(
            model_name='my_task',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 6, 14, 56, 20, 797817, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='my_task',
            name='deadline',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 6, 14, 56, 20, 878006, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='my_task',
            name='remainder_date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 6, 14, 56, 20, 878006, tzinfo=utc), help_text='add date only if remainder type is custom', null=True),
        ),
        migrations.AlterField(
            model_name='my_task',
            name='remainder_time',
            field=models.TimeField(default=datetime.datetime(2022, 1, 6, 14, 56, 20, 878006, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='my_task',
            name='time_from',
            field=models.TimeField(default=datetime.datetime(2022, 1, 6, 14, 56, 20, 878006, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='my_task',
            name='time_to',
            field=models.TimeField(default=datetime.datetime(2022, 1, 6, 14, 56, 20, 878006, tzinfo=utc)),
        ),
    ]
