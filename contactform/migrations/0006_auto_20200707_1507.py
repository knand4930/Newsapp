# Generated by Django 3.0.8 on 2020-07-07 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactform', '0005_contactform_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='time',
            field=models.CharField(max_length=10),
        ),
    ]
