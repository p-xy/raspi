#-*-coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import Template
from django.contrib import auth


def login(request):
	if request.method =='POST':
		username = request.POST['username']
		password = request.POST['password']
		#验证登录，正确则authenticate()返回一个User对象，错误则返回一个None类
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				auth.login(request, user)#登录用户
				return HttpResponseRedirect('/')#使用重定向而不是render返回首页，可以避免刷新再次提交表单导致出错
			else:
				state = '"Sorry,你的账户not is_active，请联系site.admin"'
				render(request,'login.html',{'state':state})
		else:
			state = '"oohs,你输错帐号或密码啦"'
			return render(request,'login.html',{'state':state })

	else:
		state = '”客官，登录后才能访问哦“'
	return render(request,'login.html',{'state':state})


def index(request):
	return render(request,'index.html')

def logout(request):
	return HttpResponseRedirect('/login')

