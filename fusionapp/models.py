# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db.models.functions import datetime

class CustomUser(AbstractUser):
    email = models.EmailField(max_length = 254) 
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phonenumber = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)

    # add additional fields in here

    def __str__(self):
        return self.username

class Artist(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)

class Album(models.Model):
    NONE = 'None'
    JAN = 'January'
    FEB = 'February'
    MAR = 'March'
    APR = 'April'
    MAY = 'May'
    JUN = 'June'
    JUL = 'July'
    AUG = 'August'
    SEP = 'September'
    OCT = 'October'
    NOV = 'November'
    DEC = 'December'
    MONTHS = [
        (NONE,'None'),
        (JAN,'January'),
        (FEB,'February'),
        (MAR,'March'),
        (APR,'April'),
        (MAY,'May'),
        (JUN,'June'),
        (JUL,'July'),
        (AUG,'August'),
        (SEP,'September'),
        (OCT,'October'),
        (NOV,'November'),
        (DEC,'December'),
    ]
    name = models.CharField(max_length=250)
    genre = models.CharField(max_length=150)
    month = models.CharField(max_length=30,choices=MONTHS,default=NONE)
    year = models.BigIntegerField(validators=[MinValueValidator(0000)], null=True, blank=True)

class Platform(models.Model):
    name = models.CharField(max_length=250)
    api_url = models.URLField(max_length = 200)

class Playlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    time_created = models.DateTimeField(default=datetime.datetime.now)

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    length = models.CharField(max_length=15)
    name = models.CharField(max_length=250)
    number_of_streams = models.BigIntegerField(null=True, blank=True)

