# Generated by Django 5.1.5 on 2025-01-18 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0002_event_created_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="cover_image",
            field=models.ImageField(blank=True, null=True, upload_to="event_images/"),
        ),
    ]