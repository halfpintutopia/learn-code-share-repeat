# Generated by Django 4.2.7 on 2023-12-13 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile_email_verification_token_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default='default', max_length=225, unique=True),
            preserve_default=False,
        ),
    ]
