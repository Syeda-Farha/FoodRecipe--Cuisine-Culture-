# Generated by Django 3.1.3 on 2020-11-25 06:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainApp', '0013_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='maindishes',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]