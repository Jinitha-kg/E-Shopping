# Generated by Django 4.1 on 2022-11-04 19:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_profilemodel_dob"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profilemodel",
            name="dob",
            field=models.DateField(default=datetime.date.today),
        ),
    ]
