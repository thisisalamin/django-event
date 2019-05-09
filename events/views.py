from django.shortcuts import render
from django.http import HttpResponse
from .models import Events

app_name = 'events'
# Create your views here.
def homepage(request):
    return render(request=request,template_name="event/home.html",context={"events":Events.objects.all})
def loginpage(request):
    return render(request=request,template_name="event/login.html",context={"login":Events.objects.all})
