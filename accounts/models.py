from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user   = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField()