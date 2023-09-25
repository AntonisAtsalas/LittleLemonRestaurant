from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Menu, Book
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from myapp.forms import BookingForm


# Create your views here.
def home(request):
    # Render the 'home.html' template
    return render(request, 'index.html')

def about (request):  
    about_content = {'about':'Welcome to Little Lemon Restaurant, a culinary gem nestled in the heart of the beautiful region of Chalkidiki. Our restaurant is a tribute to the art of gastronomy and the flavors that have defined this picturesque corner of Greece.'}
    return render(request,'about.html', about_content)

def menu(request):
    menu_data = Menu.objects.all().order_by('name')  # Order by name
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})

def book (request):  
    return HttpResponse('<h1> Make a booking. </h1> ')


def form_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'booking.html', context)

def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 

@api_view(['GET','POST'])
def books(request):
    response_data = {'message': 'List of books'}
    return Response(response_data, status=status.HTTP_200_OK)