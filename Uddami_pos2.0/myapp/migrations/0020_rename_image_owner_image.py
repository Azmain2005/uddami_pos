# Generated by Django 4.2.16 on 2024-12-02 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_remove_owner_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='Image',
            new_name='image',
        ),
    ]
