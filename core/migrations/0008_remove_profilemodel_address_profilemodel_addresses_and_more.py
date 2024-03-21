# Generated by Django 4.1.2 on 2022-10-29 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_rename_address_addressmodel_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profilemodel",
            name="address",
        ),
        migrations.AddField(
            model_name="profilemodel",
            name="addresses",
            field=models.ManyToManyField(to="core.addressmodel"),
        ),
        migrations.AlterField(
            model_name="profilemodel",
            name="gender",
            field=models.CharField(
                choices=[("Male", "m"), ("Female", "f"), ("Transgender", "t")],
                max_length=12,
            ),
        ),
    ]
