from django.shortcuts import render

from django.http import HttpResponse as hRes
from .models import Contact

def index(request):
    return hRes('Hello')

def display(request):
    contacts = Contact.objects.all()

    s = ""
    for c in contacts:
        s += c.to_string() + '<br>'
    
    return hRes("Contacts:<br>" + s)