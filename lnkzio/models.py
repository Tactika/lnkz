from typing import get_type_hints
from django.db import models
from django.conf import settings
from django.utils import timezone

class ShortenedURL(models.Model):
    code    = models.CharField(max_length=16, unique=True)
    url     = models.URLField(blank=True, unique=True)
    hits    = models.IntegerField(default = 0)
    
    def __str__(self):
        return str(self.url)
