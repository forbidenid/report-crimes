from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_pics', default='1.png')
    phone_no = models.CharField(max_length=10, default=00000)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


    def get_absolute_url(self):
        return reverse('accounts:dashboard')
