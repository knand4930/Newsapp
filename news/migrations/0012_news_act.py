# Generated by Django 3.0.8 on 2020-07-10 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_news_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='act',
            field=models.IntegerField(default=0),
        ),
    ]