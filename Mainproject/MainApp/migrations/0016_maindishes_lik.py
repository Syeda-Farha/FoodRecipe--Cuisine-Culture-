# Generated by Django 3.1.3 on 2020-11-25 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0015_auto_20201125_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='maindishes',
            name='lik',
            field=models.IntegerField(default=0),
        ),
    ]
