from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Category'
              
    name = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    phone = models.CharField(max_length=11, blank=False, null=False)
    email = models.EmailField(max_length=50, blank=False, null=False)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=False, null=False)
    show = models.BooleanField(default=True) 
    picture = models.ImageField( blank=True, upload_to='pictures/%Y/%m/%d')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL , null=True, blank=True )
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name