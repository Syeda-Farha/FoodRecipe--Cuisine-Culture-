# Generated by Django 3.1.3 on 2020-11-27 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0025_auto_20201127_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='maindishes',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
