# Generated by Django 3.1.6 on 2021-02-25 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20210224_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='created_on',
            field=models.TimeField(auto_now_add=True),
        ),
    ]