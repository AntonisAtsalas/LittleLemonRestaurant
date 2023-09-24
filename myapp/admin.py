from django.contrib import admin
from .models import Menu, MenuCategory, Booking, Reservation, Book

# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuCategory)
admin.site.register(Booking)
admin.site.register(Reservation)
admin.site.register(Book)
