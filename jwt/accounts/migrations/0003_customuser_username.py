# Generated by Django 4.2.7 on 2023-11-17 12:42

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_options_alter_customuser_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default=accounts.models.generate_unique_username, max_length=150, unique=True),
        ),
    ]
