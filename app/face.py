# -*- coding:utf-8 -*-
import requests

# 你的face++的应用api_key和api_secret
api_key = 'vigklkgJlKAFaSOuRfQGNcNAPz2Jrkfk'
api_secret = 'rnLgNWHIACuE6KcpWIlxf13Bc6uDpqDW'

# 接入face++ 人脸比对API
url = 'https://api-cn.faceplusplus.com/facepp/v3/compare?api_key=%s&api_secret=%s' % (api_key, api_secret)

# 载入两个本地图片进行比对
files = {
    'image_file1': open('static/img/image1.jpg', 'rb'),
    'image_file2': open('static/img/image2.jpg', 'rb'),
}

# 二进制文件，需要用post multipart/form-data的方式上传
r = requests.post(url=url, files=files)
#从json数据中获取比对值，值为[0,100]
confidence = r.json().get('confidence')

print (confidence)




