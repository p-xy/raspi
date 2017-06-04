#-*-coding:utf-8 -*-
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#这是一个继电器类，用控制门的开关
class Relay(object):
	def __init__(self,pin_number):
		self.pin_number = pin_number
		
	def open(self):
		#设置pin脚为输出
		GPIO.setup(self.pin_number,GPIO.OUT)
		#输出高电平
		GPIO.output(self.pin_number,HIGH)
		#高电平持续一秒
		time.sleep(1)
		#输出低电平继电器不工作
		GPIO.output(self.pin_number,LOW)
		#清理IO口
		GPIO.cleanup(self.pin_number)
	
		
	
		
