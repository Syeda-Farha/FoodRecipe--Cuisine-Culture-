# Generated by Django 3.1.3 on 2020-11-19 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_maindishes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maindishes',
            name='img',
            field=models.ImageField(upload_to='MainApp/static/images'),
        ),
    ]
