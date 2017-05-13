# -*- coding:utf-8 -*-

import datetime
from picamera import PiCamera

# initial a camera class
camera = PiCamera()
#picture 's name is the datetime 
now = datetime.datetime.now()
pic_name = now.strftime('%Y-%m-%d-%H-%M-%S')+'.jpg'
# picture 's address
pic_address = 'app/static/face/'
#picture
picture = pic_address + pic_name
#only user screen can start preview
camera.start_preview()
#camera need time to prepare 
time.sleep(2)
# ok,take a picture
camera.capture(picture)
#exit camera
camera.close()
print (picture)


