# Generated by Django 3.0.8 on 2020-07-14 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20200713_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='seo_keyword',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='main',
            name='seo_txt',
            field=models.CharField(default='-', max_length=200),
        ),
    ]
