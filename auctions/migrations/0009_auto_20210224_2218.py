# Generated by Django 3.1.6 on 2021-02-25 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_comment_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='created_on',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='created_on',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
