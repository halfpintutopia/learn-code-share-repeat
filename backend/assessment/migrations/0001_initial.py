# Generated by Django 4.2.7 on 2023-12-30 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0002_alter_video_image_alter_video_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('understanding', models.IntegerField(choices=[(0, 'Default'), (1, 'Just starting'), (2, 'Somewhat clear'), (3, 'Very clear'), (4, 'Fully understood')], default=0)),
                ('proficiency', models.IntegerField(choices=[(0, 'Default'), (1, 'Beginner'), (2, 'Intermediate'), (3, 'Advanced'), (4, 'Expert')], default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='videos.video')),
            ],
            options={
                'ordering': ['-created_at'],
                'unique_together': {('user', 'video')},
            },
        ),
    ]