# Generated by Django 5.1.2 on 2024-11-17 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='password',
        ),
        migrations.AddField(
            model_name='profile',
            name='contact_number',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
