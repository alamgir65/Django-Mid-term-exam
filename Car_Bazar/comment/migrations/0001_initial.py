# Generated by Django 5.0.4 on 2024-05-16 17:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car', '0004_alter_add_car_buyer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('createn_on', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='car.add_car')),
            ],
        ),
    ]