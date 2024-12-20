# Generated by Django 5.1.2 on 2024-11-20 15:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
        ('inventory', '0002_alter_car_body_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='inventory.car'),
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='start_date',
            new_name='pickup_date',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='end_date',
            new_name='return_date',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='total_price',
        ),
        migrations.AddField(
            model_name='reservation',
            name='booking_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Completed', 'Completed'), ('Canceled', 'Canceled')], default='Pending', max_length=15),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Car',
        ),
    ]
