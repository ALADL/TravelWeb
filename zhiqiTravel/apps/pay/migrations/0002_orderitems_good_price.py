# Generated by Django 2.1.2 on 2018-11-09 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitems',
            name='good_price',
            field=models.FloatField(default=0, verbose_name='单价'),
        ),
    ]
