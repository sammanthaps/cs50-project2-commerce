# Generated by Django 3.1.6 on 2021-02-19 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(help_text='Enter your comment here.', max_length=150),
        ),
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.CharField(help_text='Enter a brief description of the product.', max_length=100),
        ),
    ]
