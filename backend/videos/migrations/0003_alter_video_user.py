# Generated by Django 4.2.7 on 2023-12-30 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0002_alter_video_image_alter_video_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to=settings.AUTH_USER_MODEL),
        ),
    ]
