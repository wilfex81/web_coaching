# Generated by Django 4.1.4 on 2022-12-16 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_subscribedusers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SubscribedUsers',
            new_name='SubscribedUser',
        ),
    ]
