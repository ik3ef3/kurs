# Generated by Django 4.2.20 on 2025-04-10 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0002_client_userrole_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='menu_images/'),
        ),
    ]
