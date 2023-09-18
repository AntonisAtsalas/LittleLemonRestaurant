from django.db import models
from unicodedata import name

# Create your models here.
class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)

class Menu(models.Model):
    name = models.CharField(max_length=100)
    price  = models.IntegerField(null=False)
    
    def __str__(self):
        return self.name 

class Courses(models.Model):
    itemname = models.CharField(max_length=200)
    category = models.CharField(max_length=300)
    year  = models.IntegerField()

class Logger(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)  
    time_log = models.TimeField()

class Booking(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)  
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)

class Reservation(models.Model):
    name = models.CharField(max_length=50, blank=True)
    contact = models.CharField('Phone number', max_length=50)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name






