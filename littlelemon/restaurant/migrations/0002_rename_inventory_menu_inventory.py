# Generated by Django 5.0.3 on 2024-03-14 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='inventory',
            new_name='Inventory',
        ),
    ]
