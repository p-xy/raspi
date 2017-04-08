from django.shortcuts import render
from django.http import HttpResponse,HttpResponse
from django.template import Template

# Create your views here.

def LED_form(request):
	return render(request,"LED_form.html")


def LED_switch(request):
	LED_switch = request.GET['LED_switch']

	return render(request,'LED_switch.html',{'LED_switch':LED_switch,})

def login(request):
	return render(request,"login.html")
