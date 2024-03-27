# Generated by Django 4.2.11 on 2024-03-26 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('km_limit_per_day_info', models.CharField(max_length=100)),
                ('car_rental_depozit_amount_info', models.CharField(max_length=100)),
                ('daily_rental_price', models.IntegerField()),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='brand.brand')),
            ],
        ),
    ]
