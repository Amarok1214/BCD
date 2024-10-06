from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    password = models.TextField(blank=True, null=True)
    # Add more fields if necessary

    def __str__(self):
        return self.user.username