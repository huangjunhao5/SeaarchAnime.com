# Generated by Django 4.1.2 on 2022-10-26 03:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppUser', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blogs_user',
            new_name='AppUser',
        ),
    ]
