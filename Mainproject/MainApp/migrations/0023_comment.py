# Generated by Django 3.1.3 on 2020-11-26 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0022_remove_category_catimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('maindish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='MainApp.maindishes')),
            ],
        ),
    ]
