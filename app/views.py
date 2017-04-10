from django.shortcuts import render
from django.http import HttpResponse,HttpResponse
from django.template import Template

# Create your views here.


def LED(request):

	return render(request,'LED_form.html')

def login(request):
	return render(request,"login.html")
