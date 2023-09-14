from django import forms
from django.forms.widgets import NumberInput
from .models import Logger, Booking

class DemoForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea(attrs={'rows':2}))
    email = forms.EmailField(label='Enter email address')
    reservation_date = forms.DateField(widget=NumberInput(attrs={'type':'date'}))

class ApplicationForm(forms.Form): 
    name = forms.CharField(label='Name of Applicant', max_length=50) 
    address = forms.CharField(label='Address', max_length=100) 
    posts = (('Manager', 'Manager'),('Cashier', 'Cashier'),('Operator', 'Operator')) 
    field = forms.ChoiceField(choices=posts) 

class LogForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

   






