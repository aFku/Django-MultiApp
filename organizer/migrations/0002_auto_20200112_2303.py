# Generated by Django 3.0.2 on 2020-01-12 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]