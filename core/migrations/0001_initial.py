# Generated by Django 4.2.5 on 2023-09-10 12:14

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                ("association_id", models.CharField(max_length=38)),
                ("association_type_term", models.CharField(max_length=39)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "address_line_one",
                    models.CharField(blank=True, max_length=367, null=True),
                ),
                (
                    "address_line_two",
                    models.CharField(blank=True, max_length=367, null=True),
                ),
                ("city", models.CharField(blank=True, max_length=39, null=True)),
                ("state", models.CharField(blank=True, max_length=39, null=True)),
                ("country", models.CharField(blank=True, max_length=39, null=True)),
                ("is_delete", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]