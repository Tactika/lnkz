from django.db import models
from django.conf import settings
from django.utils import timezone

class ShortenedURL(models.Model):
    code = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    