# Generated by Django 4.1.6 on 2023-02-09 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile_first_name_userprofile_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='username',
        ),
    ]