# Generated by Django 4.2.20 on 2025-04-11 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0004_remove_menu_image_dish_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='program/media/menu_images/'),
        ),
    ]
