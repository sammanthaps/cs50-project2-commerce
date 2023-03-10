# Generated by Django 3.1.6 on 2021-02-25 05:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_auto_20210224_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='created_on',
            field=models.TimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='listing',
            name='created_on',
            field=models.TimeField(auto_now=True),
        ),
    ]
