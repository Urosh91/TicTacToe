# Generated by Django 2.0 on 2017-12-20 12:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Invitations',
            new_name='Invitation',
        ),
    ]