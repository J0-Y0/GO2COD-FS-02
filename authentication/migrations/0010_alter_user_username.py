# Generated by Django 5.1.2 on 2024-12-16 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_alter_user_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='', editable=False, max_length=255),
        ),
    ]
