# Generated by Django 3.0.8 on 2020-07-03 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='facebook',
            field=models.CharField(default='-', max_length=60),
        ),
        migrations.AddField(
            model_name='main',
            name='pinterest',
            field=models.CharField(default='-', max_length=60),
        ),
        migrations.AddField(
            model_name='main',
            name='set_name',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AddField(
            model_name='main',
            name='twitter',
            field=models.CharField(default='-', max_length=60),
        ),
        migrations.AddField(
            model_name='main',
            name='youtube',
            field=models.CharField(default='-', max_length=60),
        ),
    ]
