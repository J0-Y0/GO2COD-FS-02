# Generated by Django 5.1.2 on 2024-10-13 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_alter_product_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-last_update']},
        ),
    ]
