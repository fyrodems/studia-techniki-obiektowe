# Generated by Django 5.1.1 on 2024-10-05 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='year',
            field=models.PositiveSmallIntegerField(default=2024),
        ),
    ]