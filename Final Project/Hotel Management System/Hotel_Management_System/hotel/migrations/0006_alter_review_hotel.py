# Generated by Django 5.0.6 on 2024-07-02 18:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_alter_roomtype_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='hotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='hotel.hotel'),
        ),
    ]