# Generated by Django 3.2.4 on 2021-06-24 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_cat_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat',
            name='user',
        ),
    ]
