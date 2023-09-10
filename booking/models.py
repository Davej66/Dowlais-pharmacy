from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

FEMALE_CONSULTANT = (
    ("Yes","Yes"),
    ("No","No")
)


PHARMACIST_CHOICES = (
    ("Glynne","Glynne"),
    ("Elizabeth",("Elizabeth"))
)

PHARMACY_CHOICES = (
    ("Beacons", "Beacons"),
    ("Dowlais", "Dowlais"),
    ("Georgetown", "Georgetown"),
    ("Keir Hardie", "Keir Hardie"),
    ("Lewis", "Lewis"),
    )

SERVICE_CHOICES = (
    ("Doctor care", "Doctor care"),
    ("Nursing care", "Nursing care"),
    ("Medical social services", "Medical social services"),
    ("Homemaker or basic assistance care", "Homemaker or basic assistance care"),
    )

TIME_CHOICES = (
    ("9 AM", "9 AM"),
    ("9:30 AM", "9:30 AM"),
    ("10 AM", "10 AM"),
    ("10:30 APM", "10:30 AM"),
    ("11 AM", "11 AM"),
    ("11:30 AM", "11:30 AM"),
    ("12 PM", "12 PM"),
    ("12:30 PM", "12:30 PM"),
    ("1 PM", "1 PM"),
    ("1:30 PM", "1:30 PM"),
    ("2 PM", "2 PM"),
    ("2:30 PM", "2:30 PM"),
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
)

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    pharmacy = models.CharField(max_length=50, choices=PHARMACY_CHOICES, default="")
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="")
    preference = models.CharField(max_length=50, choices=FEMALE_CONSULTANT, default="")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="9 AM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"


