# Generated by Django 4.2.3 on 2023-07-30 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0004_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersession',
            old_name='username',
            new_name='user',
        ),
    ]
