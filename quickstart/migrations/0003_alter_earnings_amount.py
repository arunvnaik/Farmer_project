# Generated by Django 5.0.2 on 2024-02-19 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_alter_crop_time_to_grow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='earnings',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
    ]
