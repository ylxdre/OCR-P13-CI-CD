from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Model of a user of the service
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
