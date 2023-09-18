from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu

from myapp.forms import BookingForm


# Create your views here.
def home(request):
    # Render the 'home.html' template
    return render(request, 'home.html')

def about (request):  
    about_content = {'about':'Welcome to Little Lemon Restaurant, a culinary gem nestled in the heart of the beautiful region of Chalkidiki. Our restaurant is a tribute to the art of gastronomy and the flavors that have defined this picturesque corner of Greece.'}
    return render(request,'about.html', about_content)

def menu(request):
    menu_items = [
        {'name': 'Greek Salad', 'price': '12$'},
        {'name': 'Gyros', 'price': '8$'},
        {'name': 'Bouyiourdi', 'price': '6$'}
    ]
    completemenu = {'menu_items': menu_items}
    return render(request, 'menu.html', {'completemenu':completemenu})

def menu_by_id(request):
    newmenu = Menu.objects.all()
    return render(request, 'menucards.html', {'menu': newmenu})

def book (request):  
    return HttpResponse('<h1> Make a booking. </h1> ')

def menuitems(request, dish):
    items = {
        'pasta': 'very delicious meal',
        'falafel': 'not se delicious meal',
        'cheesecake': 'mid tier meal'
        }
    description = items[dish]
    return HttpResponse(f'<h2> {dish} </h2>' + description)

def drinks(request, drink):
    items = {
        'mocha': 'type of coffee',
        'tea': 'type of beverage',
        'lemonade': 'type of refreshment'
        }
    description = items[drink]
    return HttpResponse(f'<h2> {drink} </h2>' + description)

def form_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'booking.html', context)