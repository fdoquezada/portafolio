from django.shortcuts import render
from .models import project 

# Create your views here.
def home(request):
    projects = project.objects.all()

    return render(request, 'home.html', {'projects': projects})

