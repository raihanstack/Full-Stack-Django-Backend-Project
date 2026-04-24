from django.db import models
from django.contrib.auth.models import AbstractUser

class SiteUser(AbstractUser):
    ROLES = (
        ('CUSTOMER', 'Customer'),
        ('VENDOR', 'Vendor'),
        ('ADMIN', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='CUSTOMER')
    shipping_address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
    
    class Meta:
        unique_together = ('username', 'email')