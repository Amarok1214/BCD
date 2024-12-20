from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_profile')
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username
