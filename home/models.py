from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=122, blank=True, null=True)
    email = models.CharField(max_length=122, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)  # Adjust max_length for your needs
    city = models.CharField(max_length=13, blank=True, null=True)
    date = models.DateField(blank=True, null=True)  # Adjust max_length if needed
