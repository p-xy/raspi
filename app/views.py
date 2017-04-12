from django.shortcuts import render
from django.http import HttpResponse,HttpResponse
from django.template import Template

# Create your views here.

def login(request):
	return render(request,"login.html")

def index(request):
	return render(request,"index.html")


