# Generated by Django 3.1.3 on 2020-11-23 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0011_auto_20201122_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='catimg',
            field=models.ImageField(default=0, upload_to='MainApp/static/MainApp/images'),
        ),
    ]