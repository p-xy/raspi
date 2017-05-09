#-*-coding:utf-8 -*-

from django.shortcuts import render,redirect
from django.template import Template
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import requests
import json
import time

from picamera import PiCamera
import RPi.GPIO as GPIO
from .models import LED_FORM
from hardware.led import LED
from hardware import dht11



# 主页
@login_required()
def index(request):
	if request.method == 'POST':
		face_or_camera = request.POST['face_or_camera']
		if face_or_camera ==u'人脸比对':
			# 你的face++的应用api_key和api_secret
			api_key = 'vigklkgJlKAFaSOuRfQGNcNAPz2Jrkfk'
			api_secret = 'rnLgNWHIACuE6KcpWIlxf13Bc6uDpqDW'

			# 接入face++ 人脸比对API
			url = 'https://api-cn.faceplusplus.com/facepp/v3/compare?api_key=%s&api_secret=%s' % (api_key, api_secret)

			# 载入两个本地图片进行比对
			files = {
				'image_file1': open('app/static/img/image1.jpg', 'rb'),
				'image_file2': open('app/static/img/image2.jpg', 'rb'),
			}

			# 二进制文件，需要用post multipart/form-data的方式上传
			r = requests.post(url=url, files=files)
			#从json数据中获取比对值，值为[0,100]
			confidence = r.json().get('confidence')
			JSON = r.json()

			return render(request,'index.html',{ 'JSON':JSON,'confidence':confidence })
			
		elif face_or_camera ==u'拍个照片':
			
			#实例化一个相机类
			camera = PiCamera()
			
			camera.resolution = (1900,1080)
			camera.start_preview()
			#相机启动需要一定时间
			time.sleep(2)
			#拍取一张照片，保存在app/static/img目录下
			camera.capture('app/static/img/image2.jpg')
			#关闭相机
			camera.close()
			
			return redirect('/')
	
	return render(request,'index.html')
			


#查看
@login_required()
def look(request):
	#读取LED开关值
	p1 = LED_FORM.objects.get(id=1)	#id为LED_FORM表单的外键，存储的开关值的列为switch
	#把开关值传递给p2，以上下文方式提交到模板
	p2 = p1.switch
	
	# DHT11温/湿度传感器数据
	instance = dht11.DHT11(8)
	result = instance.read()
	if result.is_valid():
		''' p4 ="Last valid input: " + str(datetime.datetime.now()) '''
		
        p5 = "温度: %d ℃" % result.temperature
        p6 = "湿度: %d %%" % result.humidity
        GPIO.cleanup(8)
        	
	return render(request,'look.html',{ 'p2':p2 ,'p5':p5,'p6':p6 })
	
	

#控制
@login_required()
def control(request):	
			
	if request.method=="POST":
		''' LED'''
		#读取表单提交数据
		state = request.POST.get('switch')
		#把开关数据存储到数据库
		p1 = LED_FORM.objects.get(id=1)
		#switch为存储开关值的列
		p1.switch=state
		p1.save()
		#实例化一个LED类
		led = LED(40,state)
		#LED.switch（）为LED类的开关控制方法
		led.switch()		
		return render(request,'control.html',{'state':state })				
				
	else:
		
		return render(request,'control.html')

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



