# Generated by Django 3.1.7 on 2021-03-16 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='rounds_completed',
            field=models.IntegerField(default=0),
        ),
    ]
