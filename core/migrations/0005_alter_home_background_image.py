# Generated by Django 4.1.4 on 2022-12-15 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_home_background_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='background_Image',
            field=models.ImageField(upload_to='background_images'),
        ),
    ]