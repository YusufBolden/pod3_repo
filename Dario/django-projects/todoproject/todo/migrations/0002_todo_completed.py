# Generated by Django 3.2.8 on 2021-11-05 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
