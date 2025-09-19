from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.
class Contact(models.Model):
    #this line creates a one-to-one relationship with the built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    
    phone_number = models.CharField(max_length=20)
    
    def __str_(self):
        return f"{self.user.username}"
   