# Generated by Django 5.1.4 on 2025-02-06 20:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(blank=True, max_length=40, null=True)),
                ('ticket', models.CharField(max_length=20, unique=True)),
                ('start_park', models.DateTimeField(blank=True, null=True)),
                ('end_park', models.DateTimeField(blank=True, null=True)),
                ('total_price', models.IntegerField(default=0)),
                ('is_complete', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.categorymodel')),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.slotmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.userprofile')),
            ],
        ),
    ]
