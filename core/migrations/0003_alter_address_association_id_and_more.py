# Generated by Django 4.2.5 on 2023-09-24 11:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_add_groups"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="association_id",
            field=models.CharField(blank=True, max_length=38, null=True),
        ),
        migrations.AlterField(
            model_name="address",
            name="association_type_term",
            field=models.CharField(blank=True, max_length=39, null=True),
        ),
    ]