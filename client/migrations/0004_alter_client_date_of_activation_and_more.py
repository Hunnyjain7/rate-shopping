# Generated by Django 4.2.5 on 2023-11-08 19:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("client", "0003_alter_client_code_alter_client_is_enable"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="date_of_activation",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="client",
            name="date_of_renewal",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]