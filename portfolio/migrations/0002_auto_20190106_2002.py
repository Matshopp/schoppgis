# Generated by Django 2.1.5 on 2019-01-06 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolioitem',
            old_name='role',
            new_name='roles',
        ),
    ]