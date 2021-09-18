from django.db import models
from django.utils import timezone
# Create your models here.

class location(models.Model):
    location = models.CharField(max_length=96, blank=True ,null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location