# Generated by Django 2.1.5 on 2019-01-08 18:07

from django.db import migrations, models
import django.db.models.deletion
import portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_portfolioitem_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=portfolio.models.get_image_filename, verbose_name='Image')),
                ('portfolio_item', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='portfolio.PortfolioItem')),
            ],
        ),
    ]