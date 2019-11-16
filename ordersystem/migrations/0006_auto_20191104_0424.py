# Generated by Django 2.2.6 on 2019-11-04 04:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ordersystem', '0005_auto_20191104_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 4, 4, 24, 21, 660313, tzinfo=utc)),
        ),
    ]