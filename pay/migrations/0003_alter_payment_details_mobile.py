# Generated by Django 3.2.6 on 2021-08-30 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0002_alter_payment_details_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_details',
            name='mobile',
            field=models.CharField(max_length=10, verbose_name='Phone NO'),
        ),
    ]
