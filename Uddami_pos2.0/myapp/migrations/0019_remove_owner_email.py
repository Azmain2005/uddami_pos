# Generated by Django 4.2.16 on 2024-12-01 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_flat_district_flat_upazila'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='email',
        ),
    ]
