# Generated by Django 3.0.6 on 2020-09-29 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_bridge', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='image',
            field=models.ImageField(unique=True, upload_to='images/'),
        ),
    ]
