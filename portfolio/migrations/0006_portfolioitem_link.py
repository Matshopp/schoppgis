# Generated by Django 2.1.5 on 2019-01-13 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_accomplishment'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioitem',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
