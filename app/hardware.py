# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time


'''
	There has two ways of numbering the IO pins on a
	Rsapberry Pi within RPi.GPIO : "BOARD" and "BCM" .
	More detail , just google "the wiki of RPi.GPIO".
'''
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

class LED(object):
	'''	
		pin_number is your IO pins number. 
		open_or_close is the switch for controll LED.
	'''
	def __init__(self,pin_number,open_or_close):
		self.pin_number = pin_number
		self.open_or_close = open_or_close
	
	
	def switch(self):
		GPIO.setup(self.pin_number,GPIO.OUT)# set up the channel as output.
				
		if self.open_or_close == '开':
			GPIO.output(self.pin_number,GPIO.HIGH)
			
		elif self.open_or_close == '关':
			GPIO.output(self.pin_number,GPIO.LOW)
		
				
										#GPIO.output(self.pin_number,GPIO.HIGH) #another pin has been connected to Ground pin,so HIGH is open.
			
			
	
	
	



