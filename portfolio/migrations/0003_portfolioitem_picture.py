# Generated by Django 2.1.5 on 2019-01-07 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20190106_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioitem',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
