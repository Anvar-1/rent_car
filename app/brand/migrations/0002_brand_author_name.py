# Generated by Django 4.2.11 on 2024-03-29 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='author_name',
            field=models.CharField(default='author', max_length=255),
            preserve_default=False,
        ),
    ]