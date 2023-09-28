# Generated by Django 4.2.4 on 2023-09-22 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_userprofile_default_prescription'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_pharmacy',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='default_prescription',
            field=models.CharField(blank=True, choices=[('Deliver prescriptions', (('Y', 'Yes, Prescription to be delivered'), ('N', 'No, Prescription not to be delivered')))], max_length=5, null=True),
        ),
    ]