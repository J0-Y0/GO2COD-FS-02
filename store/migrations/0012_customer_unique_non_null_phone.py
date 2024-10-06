# Generated by Django 5.1.1 on 2024-10-06 14:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_productimage_image_alter_productimage_product'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='customer',
            constraint=models.UniqueConstraint(condition=models.Q(('phone__isnull', False)), fields=('phone',), name='unique_non_null_phone'),
        ),
    ]
