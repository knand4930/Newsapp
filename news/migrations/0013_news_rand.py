# Generated by Django 3.0.8 on 2020-07-11 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_news_act'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='rand',
            field=models.IntegerField(default=0),
        ),
    ]
