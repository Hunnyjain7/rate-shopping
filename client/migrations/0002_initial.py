# Generated by Django 4.2.5 on 2023-09-10 12:14

import django.db.models.deletion
import django.db.models.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("core", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("client", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="activation_by",
            field=models.ForeignKey(
                on_delete=django.db.models.fields.DateField,
                related_name="activation_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="client",
            name="address",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="core.address"
            ),
        ),
        migrations.AddField(
            model_name="client",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]