# Generated by Django 3.2.20 on 2023-07-13 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='users_answered',
            field=models.ManyToManyField(default=None, null=True, to='authentication.Users'),
        ),
    ]
