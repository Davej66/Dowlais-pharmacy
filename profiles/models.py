from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField





class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history

    """
    PRES_CHOICES = [('Deliver prescriptions',(
        ('Y', 'Yes, Prescription to be delivered'),
        ('N', 'No, Prescription not to be delivered'),
    ))]

    PHARMA_CHOICES = [('Pharmacy',(
        ('Beacons', 'Beacons Pharmacy'),
        ('Dowlais', 'Dowlais Pharmacy'),
        ('Georgetown', 'Georgetown Pharmacy'),
        ('Keir Hardie', 'Keir Hardie Pharmacy'),
        ('Lewis', 'Lewis Pharmacy'),
    ))]


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_prescription = models.CharField(max_length=5, null=True, blank=True, choices=PRES_CHOICES)
    default_pharmacy = models.CharField(max_length=20, null=True, blank=True, choices=PHARMA_CHOICES)
    default_ni = models.CharField(max_length=20, null=True, blank=True)
    default_medicaln = models.CharField(max_length=20, null=True, blank=True)
    default_gpsurgey = models.CharField(max_length=20, null=True, blank=True)
    default_doctor = models.CharField(max_length=20, null=True, blank=True)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)
    default_email = models.CharField(max_length=20, null=True, blank=True)


    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
