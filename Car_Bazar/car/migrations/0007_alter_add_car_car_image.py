# Generated by Django 5.0.4 on 2024-05-17 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_alter_add_car_car_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_car',
            name='car_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]