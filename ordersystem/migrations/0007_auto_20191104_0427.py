# Generated by Django 2.2.6 on 2019-11-04 04:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ordersystem', '0006_auto_20191104_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 4, 4, 27, 51, 539291, tzinfo=utc)),
        ),
    ]