from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    phone = models.CharField(max_length=11, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=False, null=False) 

