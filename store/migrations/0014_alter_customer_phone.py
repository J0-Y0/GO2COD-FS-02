# Generated by Django 5.1.1 on 2024-10-06 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_remove_customer_unique_non_null_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
