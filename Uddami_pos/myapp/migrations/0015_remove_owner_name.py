# Generated by Django 4.2.16 on 2024-11-24 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_remove_flat_owner_flat_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='name',
        ),
    ]
