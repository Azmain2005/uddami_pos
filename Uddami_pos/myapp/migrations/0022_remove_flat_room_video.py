# Generated by Django 4.2.16 on 2024-12-02 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_alter_flat_house_cover_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='room_video',
        ),
    ]
