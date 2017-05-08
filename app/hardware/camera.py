# -*- coding:utf-8 -*-

from picamera import PiCamera
import time
camera = PiCamera()
camera.brightness = 50
camera.start_preview()
time.sleep(3)

camera.capture('image.jpg')




