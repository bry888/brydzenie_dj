# Generated by Django 2.2.3 on 2019-07-30 15:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bryopo', '0003_auto_20190730_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emaile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 30, 15, 3, 6, 503619, tzinfo=utc), verbose_name='created_date'),
        ),
        migrations.AlterField(
            model_name='oposy',
            name='opo_title',
            field=models.CharField(max_length=200, verbose_name='opo_title'),
        ),
    ]
