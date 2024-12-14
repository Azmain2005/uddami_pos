# Generated by Django 4.2.16 on 2024-11-21 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_flat_owner_roomimage_remove_users_courses_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='flats',
        ),
        migrations.AddField(
            model_name='flat',
            name='owner',
            field=models.ManyToManyField(related_name='flats', to='myapp.owner'),
        ),
    ]
