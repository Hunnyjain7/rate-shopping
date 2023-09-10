# Generated by Django 4.2.5 on 2023-09-10 12:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('seq_number', models.PositiveIntegerField(auto_created=True, editable=False, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, max_length=38, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=38, null=True)),
                ('date_of_activation', models.DateTimeField()),
                ('date_of_renewal', models.DateTimeField()),
                ('client_name', models.CharField(max_length=350)),
                ('code', models.CharField(default='CLI40571208', editable=False, max_length=15)),
                ('contact_name', models.CharField(blank=True, max_length=350, null=True)),
                ('date_of_registration', models.DateTimeField(editable=False)),
                ('client_status_term', models.CharField(blank=True, max_length=39, null=True)),
                ('relation_manager_id', models.CharField(blank=True, max_length=39, null=True)),
                ('total_competitors', models.PositiveIntegerField(default=0)),
                ('total_corporates', models.PositiveIntegerField(default=0)),
                ('total_properties', models.PositiveIntegerField(default=0)),
                ('last_contacted', models.DateTimeField(blank=True, null=True)),
                ('is_enable', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
