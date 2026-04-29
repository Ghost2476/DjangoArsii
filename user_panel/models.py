from django.db import models
from accounts.models import CustomUser

class Profile(models.Model):
    user    = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    phone   = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
