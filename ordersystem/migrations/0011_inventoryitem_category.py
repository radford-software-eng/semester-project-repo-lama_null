# Generated by Django 2.2.6 on 2019-11-14 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersystem', '0010_auto_20191111_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='category',
            field=models.CharField(default='Miscellaneous', max_length=30),
        ),
    ]
