# Generated by Django 3.1.3 on 2020-11-26 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0020_login_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maindishes',
            name='lik',
        ),
        migrations.RemoveField(
            model_name='maindishes',
            name='likes',
        ),
    ]
