# Generated by Django 5.1.2 on 2024-12-04 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('gcash', 'GCash'), ('paypal', 'PayPal'), ('card', 'Card')], max_length=10)),
                ('account_number', models.CharField(max_length=20)),
                ('cardholder_name', models.CharField(blank=True, max_length=100, null=True)),
                ('expiry_date', models.CharField(blank=True, max_length=7, null=True)),
                ('cvc', models.CharField(blank=True, max_length=4, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
