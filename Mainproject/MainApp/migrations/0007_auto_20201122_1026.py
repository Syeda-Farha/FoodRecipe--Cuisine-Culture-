# Generated by Django 3.1.3 on 2020-11-22 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_auto_20201121_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maindishes',
            name='descr',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='maindishes',
            name='steps',
            field=models.TextField(default='none'),
        ),
    ]
