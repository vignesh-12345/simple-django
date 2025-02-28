from django.shortcuts import render
from travel1 import templates
from .models import Destination
# Create your views here.
def index(request):
           
    dests = Destination.objects.all()

    return render(request,"index.html",{'dests':dests})
