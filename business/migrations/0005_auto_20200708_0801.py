# Generated by Django 3.0.5 on 2020-07-08 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_auto_20200707_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryboyjob',
            name='is_registered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shoponline',
            name='is_registered',
            field=models.BooleanField(default=False),
        ),
    ]