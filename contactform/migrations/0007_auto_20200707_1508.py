# Generated by Django 3.0.8 on 2020-07-07 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactform', '0006_auto_20200707_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='date',
            field=models.CharField(max_length=12),
        ),
    ]
