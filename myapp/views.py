from django.shortcuts import render
from django.http import HttpResponse

from myapp.forms import BookingForm


# Create your views here.
def home(request):
    return HttpResponse('<h1> Welcome to Little Lemon! </h1> ')

def about (request):  
    return HttpResponse('<h1> About us </h1> ')

def menu (request):  
    return HttpResponse('<h1> Menu for Little Lemon </h1> ')

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