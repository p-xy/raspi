from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Template
from .models import User

# Create your views here.

def login(request):
	if request.method =='POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = User.objects.filter(email__exact=email,password__exact=password)
		if user:
			return render(request,'index.html')
		else:
			return HttpResponse('<h1>bad input</h1>')

	return render(request,'login.html')


def index(request):
	return render(request,"index.html")


