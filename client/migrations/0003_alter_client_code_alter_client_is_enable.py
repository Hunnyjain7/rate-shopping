# Generated by Django 4.2.5 on 2023-11-05 17:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("client", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="code",
            field=models.CharField(editable=False, max_length=15),
        ),
        migrations.AlterField(
            model_name="client",
            name="is_enable",
            field=models.BooleanField(default=True),
        ),
    ]
