# Generated by Django 3.0.8 on 2020-07-13 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20200710_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='name',
            field=models.TextField(default=''),
        ),
    ]
