# Generated by Django 2.2.3 on 2019-07-29 13:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bryopo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emaile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 29, 13, 30, 53, 51215, tzinfo=utc), verbose_name='created_date'),
        ),
    ]
