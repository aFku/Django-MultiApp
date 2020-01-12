# Generated by Django 3.0.2 on 2020-01-12 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=500)),
                ('time', models.DateField(blank=True, null=True)),
                ('eventype', models.CharField(choices=[('M', 'Meeting'), ('B', 'Birthday party'), ('L', 'Lecture'), ('S', 'Shopping time'), ('N', 'Netflix alert'), ('O', 'Other')], default='O', max_length=1)),
            ],
        ),
    ]
