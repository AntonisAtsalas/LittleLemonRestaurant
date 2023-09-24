from django.db import models
from unicodedata import name

# Create your models here.
class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)

class Menu(models.Model):
    name = models.CharField(max_length=100)
    price  = models.IntegerField(null=False)
    description = models.CharField(max_length=200,default='')
    
    def __str__(self):
        return self.name 


class Booking(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)  
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)
    
    def __str__(self):
      return self.first_name + ' ' + self.last_name

class Reservation(models.Model):
    name = models.CharField(max_length=50, blank=True)
    contact = models.CharField('Phone number', max_length=50)
    time = models.TimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author  =  models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    class Meta:
        indexes = models.Index(fields=['price']),

    def __str__(self):
        return self.name   






