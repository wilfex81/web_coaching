# Generated by Django 4.1.4 on 2022-12-21 09:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonie',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='testimonies_images'),
            preserve_default=False,
        ),
    ]
