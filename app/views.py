#-*-coding:utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import Template
from django.contrib import auth

# 用户登录
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
				NOT_ACTIVE = '你的账户没有激活，请联系管理员'
				render(request,'login.html',{'NOT_ACTIVE':NOT_ACTIVE})
		else:
			ERROR = '唉呀好气呀,输入有误'
			return render(request,'login.html',{'ERROR':ERROR })

	else:
		LOGIN = '客官，登录后才能访问噢'
	return render(request,'login.html',{'LOGIN':LOGIN})

# 主页
def index(request):
	return render(request,'index.html')

#退出
def logout(request):
	return HttpResponseRedirect('/login')

