# Generated by Django 2.2.1 on 2019-05-09 06:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=250)),
                ('event_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='event date')),
                ('event_location', models.CharField(max_length=250)),
                ('event_description', models.TextField()),
            ],
        ),
    ]