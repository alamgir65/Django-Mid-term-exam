# Generated by Django 5.0.4 on 2024-05-16 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0001_initial'),
        ('car', '0002_add_car_car_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_car',
            name='buyer',
            field=models.ManyToManyField(blank=True, to='buyer.buyer'),
        ),
        migrations.AlterField(
            model_name='add_car',
            name='car_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
