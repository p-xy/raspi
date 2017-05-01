#-*-coding:utf-8 -*-

from django.shortcuts import render,redirect
from django.template import Template
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from hardware import LED
from threading import Thread

# 登录
def login(request):
	if request.method =='POST':
		username = request.POST['username']
		password = request.POST['password']
		#验证登录，正确则authenticate()返回一个User对象，错误则返回一个None类
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth.login(request, user)#登录用户
				return redirect('/',{'username':username})#使用重定向而不是render返回首页，可以避免刷新再次提交表单导致出错
			else:
				NOT_ACTIVE = '你的账户没有激活，请联系管理员'
				render(request,'login.html',{'NOT_ACTIVE':NOT_ACTIVE})
		else:
			ERROR = 'Typing Error'
			return render(request,'login.html',{'ERROR':ERROR })

	else:
		LOGIN = 'Login System'
	return render(request,'login.html',{'LOGIN':LOGIN})

# 主页
@login_required()
def index(request):

	return render(request,'index.html')


#查看
@login_required()
def look(request):
	return render(request,'look.html')
	
	

#控制
@login_required()
def control(request):	
			
	if request.method=="POST":
		''' LED'''
		state = request.POST.get('switch')
		led = LED(40,state)
		led.switch()		
		return render(request,'control.html',{'state':state })				
				
	else:
		
		return render(request,'control.html')

#退出
def logout(request):
	auth.logout(request)
	return redirect('/login')





