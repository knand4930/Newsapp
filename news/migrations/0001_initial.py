# Generated by Django 3.0.8 on 2020-07-04 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('short_txt', models.TextField()),
                ('body_txt', models.TextField()),
                ('date', models.CharField(max_length=12)),
                ('pic', models.TextField()),
                ('picurl', models.TextField()),
                ('writer', models.CharField(max_length=50)),
                ('email', models.TextField(default='-')),
                ('email1', models.TextField(default='-')),
            ],
        ),
    ]