# Generated by Django 5.0.2 on 2024-03-30 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_jobapplication_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='self_made',
            field=models.BooleanField(default=False),
        ),
    ]