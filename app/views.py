#-*-coding:utf-8 -*-

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Template
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import requests
import json
import time
import datetime
from picamera import PiCamera
import RPi.GPIO as GPIO
from .models import LED_FORM
from hardware.led import LED
from hardware import dht11


#拍照功能
@login_required()
def take_a_photo(request):
	# 实例化一个相机类
	camera = PiCamera()

	#照片名由时间组成
	now = datetime.datetime.now()
	face_name = now.strftime('%Y-%m-%d-%H-%M-%S')+'.jpg'

	# 拍好照片的存放地址
	face_address = 'app/static/face/'

	#拍一个照片需要提供照片名和存放地址
	face = face_address + face_name

	#需要把刚拍的照片返回给ajax以更新客户端的图片，但模板的img src不需要app/后缀
	img = "/static/face/" + face_name

	#设置相机的分辨率
	camera.resolution = (1900,1080)
	#相机预览，很可惜只有接上显示屏才能预览，ssh方式无法预览
	camera.start_preview()

	#相机启动需要点时间
	time.sleep(2)
	# 拍照，把大小裁剪为1024x768，太大不适合提交给人脸比对
	camera.capture(face,resize=(1024,768))
	
	#关闭相机，否则http一直在连接
	camera.close()
	#返回照片名以更新客户端照片
	return HttpResponse(img)
	

#人脸比对功能
@login_required()
def face_compare(request):
	#获取要人脸比对的两张图片，加上app/后缀才能在服务端找到本地图片
	face1 = 'app/' + request.GET['img1']
	face2 = 'app/' + request.GET['img2']
	# face++的应用api_key和api_secret
	api_key = 'vigklkgJlKAFaSOuRfQGNcNAPz2Jrkfk'
	api_secret = 'rnLgNWHIACuE6KcpWIlxf13Bc6uDpqDW'
	# 接入face++ 人脸比对API
	url = 'https://api-cn.faceplusplus.com/facepp/v3/compare?api_key=%s&api_secret=%s' % (api_key, api_secret)	
	# 载入两个本地图片进行比对
	files = {
			'image_file1': open(face1, 'rb'),
			'image_file2': open(face2, 'rb'),
		}

	# 二进制文件，需要用post multipart/form-data的方式上传
	r = requests.post(url=url, files=files)	
	#人脸比对的response，是一个json包
	data = r.json()
	#人脸数据，若识别不出人脸则为空list
	faces1 = data.get('faces1')
	faces2 = data.get('faces2')
	#格式化json数据，以便在html中展示
	JSON = json.dumps(data,indent=1)
		
	print('--------------------------')
	print(data)
	# 若人脸能识别出来，则face1/2事非空list
	if (len(faces1) != 0 ) and (len(faces2) != 0):
		#认证系数，[0,100]，大于60则可认为是同一个人
		confidence = data.get('confidence')
		if confidence >= 60:	
				
			compare_result = '很大可能是同一个人'
			result={ 'compare_result':compare_result,'JSON':JSON }
			return JsonResponse(result)
		
		elif confidence<60:
			
			compare_result = '很大可能不是同一个人'
			result = {'compare_result':compare_result,'JSON':JSON }
			return JsonResponse(result)
	else :
		
		compare_result = '未能检测到人脸'
		result = {'compare_result':compare_result,'JSON':JSON }
		#使用JsonResponse能更好的返回json数据
		return JsonResponse(result)
		



#人脸比对的页面
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
	
	if request.method == 'POST':
		
		# DHT11温/湿度传感器数据
		instance = dht11.DHT11(8)
		result = instance.read()
		
		if result.is_valid():
			temp = "%d ℃" % result.temperature
			hum = "%d %%" % result.humidity
			GPIO.cleanup(8)			
			return JsonResponse({ 'temperature':temp,'humidity':hum })
		else:
			return HttpResponse('error')
			
			
		
	else:
				
		#读取LED开关值,id为LED_FORM表单的外键，存储的开关值的列为switch
		led = LED_FORM.objects.get(id=1)	
		#把开关值传递给LED，以上下文方式提交到模板
		LED = led.switch
		
		# DHT11温/湿度传感器数据
		instance = dht11.DHT11(8)
		result = instance.read()
		
		temp = " %d ℃" % result.temperature
		hum = " %d %%" % result.humidity
		GPIO.cleanup(8)
						
		return render(request,'look.html',{ 'LED':LED ,'temperature':temp,'humidity':hum })
	
	

#控制LED
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
		response = u'灯已:'+state	
		return HttpResponse(response)
				
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



