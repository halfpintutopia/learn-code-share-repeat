# Generated by Django 4.2.7 on 2023-12-29 21:11

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_profile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='background_image',
            field=models.ImageField(blank=True, null=True, storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='profile_background_image', verbose_name='Background image'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='profile_image', verbose_name='Profile image'),
        ),
    ]
