# Generated by Django 5.0.2 on 2024-02-20 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0007_remove_earnings_crop'),
    ]

    operations = [
        migrations.AddField(
            model_name='earnings',
            name='crop',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='earnings', to='quickstart.crop'),
            preserve_default=False,
        ),
    ]
