# Generated by Django 3.2.17 on 2023-02-21 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('license_plate', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=100)),
                ('first_responder', models.CharField(max_length=100)),
                ('vehicle_type', models.CharField(max_length=100)),
            ],
        ),
    ]
