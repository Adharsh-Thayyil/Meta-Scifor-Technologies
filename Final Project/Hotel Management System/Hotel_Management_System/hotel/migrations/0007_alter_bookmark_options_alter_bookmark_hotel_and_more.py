# Generated by Django 5.0.6 on 2024-07-02 19:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_alter_review_hotel'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmark',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='hotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel'),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]