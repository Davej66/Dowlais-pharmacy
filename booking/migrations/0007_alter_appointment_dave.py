# Generated by Django 4.2.4 on 2023-09-19 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_appointment_dave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='dave',
            field=models.CharField(choices=[('MONDAY', 'MONDAY'), ('TUESDAY', 'TUESDAY'), ('WEDNESNDAY', 'WEDNESDAY'), ('THURSDAY', 'THURSDAY'), ('FRIDAY', 'FRIDAY'), ('SATURDAY', 'SATURDAY'), ('SUNDAY', 'SUNDAY')], default='MONDAY', max_length=50),
        ),
    ]