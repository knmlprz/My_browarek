# Generated by Django 5.0.4 on 2024-04-13 15:30

import datetime
import user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birthDate',
            field=models.DateField(default=datetime.datetime(2024, 4, 13, 15, 30, 54, 325201, tzinfo=datetime.timezone.utc), validators=[user.models.validate_birth_date]),
        ),
    ]
