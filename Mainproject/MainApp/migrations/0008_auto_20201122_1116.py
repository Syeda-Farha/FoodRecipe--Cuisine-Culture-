# Generated by Django 3.1.3 on 2020-11-22 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0007_auto_20201122_1026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maindishes',
            old_name='descr',
            new_name='ingred',
        ),
    ]
