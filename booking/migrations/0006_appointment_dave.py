# Generated by Django 4.2.4 on 2023-09-19 14:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_alter_appointment_preference_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='dave',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
