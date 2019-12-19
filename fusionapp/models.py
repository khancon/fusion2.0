# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    email = models.EmailField(max_length = 254) 
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phonenumber = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    # add additional fields in here

    def __str__(self):
        return self.username