#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Template
from django.contrib import auth
from django.contrib.auth.decorators import login_required

@login_required()
def face(request):
	return render(request,'face.html')


# 主页
@login_required()
def index(request):
	return render(request,'index.html')

#查看状态
@login_required()
def look(request):
    return render(request,'look.html')

#退出
def logout(request):
	auth.logout(request)
	return redirect('/login')

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

#控制LED
@login_required()
def control(request):	
    return render(request,'control.html')

#人脸比对的页面
@login_required()
def face(request):
	return render(request,'face.html')