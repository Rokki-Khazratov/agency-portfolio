# Generated by Django 5.0.2 on 2024-03-13 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_service_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='thumbnail_image',
            field=models.ImageField(default=1, upload_to='thumbnail_images/'),
            preserve_default=False,
        ),
    ]
