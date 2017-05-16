# -*- coding:utf-8 -*-
import sys #要重新载入sys。因为 Python 初始化后会删除 sys.setdefaultencoding 这个方 法
import os
import requests
import json

reload(sys) 
sys.setdefaultencoding('utf-8')

 #百度TTS地址
base_url = "https://openapi.baidu.com/oauth/2.0/token"
 #必填
grant_type="client_credentials"
 #应用 id
client_id = "fxzDws6WnsGyezimouPecYzz"
 #应用 secret
client_secret = "a417b0cd621c21a396e057538e0622f6"
#响应用的url 
url = "%s?grant_type=%s&client_id=%s&client_secret=%s&" % (base_url, grant_type,client_id,client_secret)
#获取响应
r = requests.post(url=url)
data = r.json()
#拿到access_token，用于语音合成
access_token = data["access_token"]

#access_token = '24.e424356c9a2ce71d33069d0da8802ffc.2592000.1497505014.282335-9650693'


JSON = json.dumps(data,indent=1)
print(access_token)

#--------------语音合成
url_1 =  'http://tsn.baidu.com/text2audio'
tex1 = '当前正在请求拍照，请保持微笑姿势'
tex2 = '真正在进行人脸比对，请稍等'
lan = 'zh'
tok = access_token
ctp = 1
cuid = '28-D2-44-02-98-59'

camera_url = '%s?tex=%s&lan=%s&tok=%s&ctp=1&cuid=%s' % (url_1,tex1,lan,tok,cuid)
face_url = '%s?tex=%s&lan=%s&tok=%s&ctp=1&cuid=%s' % (url_1,tex2,lan,tok,cuid)


os.system(' mpg123 "%s" ' % (face_url))


