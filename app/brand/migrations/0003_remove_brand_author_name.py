# Generated by Django 4.2.11 on 2024-04-03 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0002_brand_author_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='author_name',
        ),
    ]
