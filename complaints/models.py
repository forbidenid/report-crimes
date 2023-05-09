from django.db import models
from . choices import CRIME_CATEGORY
from django.urls import reverse
from Test import settings
from django.template.defaultfilters import slugify


class Complaint(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    seen_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='supervisor', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    category = models.IntegerField(choices=CRIME_CATEGORY, default=1)
    description = models.TextField(max_length=200)
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('accounts:dashboard')

    def __str__(self):
        return self.title