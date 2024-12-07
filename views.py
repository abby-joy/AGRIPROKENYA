from django.shortcuts import render
from .models import Equipment

def home_view(request):
    return render(request, 'home/index.html') 

def contact_view(request):
    return render(request, 'home/contact.html')

def equipments_view(request):
    equipments = Equipment.objects.all() 
    return render(request, 'home/equipment.html', {'equipments': equipments})