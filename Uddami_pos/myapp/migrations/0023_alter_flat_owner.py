# Generated by Django 4.2.16 on 2024-12-03 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_remove_flat_room_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='owner',
            field=models.ForeignKey(default=-11, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='flats', to='myapp.owner'),
        ),
    ]
