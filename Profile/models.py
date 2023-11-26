from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    # groups = models.ManyToManyField(Group, related_name="customuser_set", blank=True)
    # user_permissions = models.ManyToManyField(
    #     Permission, related_name="customuser_set", blank=True
    # )

    def __str__(self):
        return self.username
