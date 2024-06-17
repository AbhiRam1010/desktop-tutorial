from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from .forms import *


# Create your views here.
def SchoolRegister(request):
    ESFO=SchoolForm()
    d={'ESFO':ESFO} 
    if request.method == 'POST':
        SFDO=SchoolForm(request.POST)
        SFDO.save()
        return HttpResponse('Hela bodhe')
           
    return render (request,'register.html',d)