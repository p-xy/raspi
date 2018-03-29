# 《基于树莓派的智能家居监控系统》

## 简介
raspi是我本科毕业论文的一个paper，从2017年3月到6月份完成，对于一个没怎么接触软件领域的微电子学生来说已经是一个天大的工程！毕业万岁~\(≧▽≦)/~

关于这个project：
- software：主要使用了 python2.7 + django1.11 + bootstrap3.3 
- hardware：树莓派3B+、摄像头、继电器、DHT11温湿度传感器、LED等等
- 系统环境：基于debian7定制的树莓派官方系统raspbian
- 第三方接入：face++人脸比对、百度tts文字转语音

实际上软件部分还用到了树莓派的官方系统raspbian提供的驱动，比如摄像头驱动模块picamera、IO接口模块RPi.GPIO。因此，原理上clone这个repository到本地pc上是无法running的，需要做一些修改，后面会提到。

## 功能
- 访问权限：只有登录才能进入web页面，控制家居设备。
- 温湿度实时监控
- face++d人脸比对 + 百度语音 +继电器 实现安全门禁,刷脸开门！
- 控制家电开关：这里只实现了LED模拟家庭环境

实际上我还接入了google-assistant的SDK，可以chat with google assistant～，但由于当时google-assistant才刚开放(没错就是在github),还处于测试阶段，接入语音控制这些功能都还没有，语音助手纯属就是一个玩具；(


## 页面展示
#### 首页
![home](app/static/img/home.png)
#### 人脸比对
![face](app/static/img/face.png)
#### 查看温湿度
![look](app/static/img/look.png)
#### LED模拟控制室内灯光
![LED](app/static/img/control.png)
#### 登录界面
![login](app/static/img/login.png)


## 如何在本地运行
- 安装django1.11 + python2.7 ，注意django的2.0版本和1版本不兼容。
- clone到本地：
> 1. app/urls.py把 from . import views 改成 from . import cp_views as views 。  
> 2. app/urls.py 把最后这两行注释：
    <p>url(r'^take_a_photo$',views.take_a_photo)</p>
    <p>url(r'^face_compare$',views.face_compare)</p>
> 3. 运行：
    <p>$python manage.py makemigrations</p>
    <p>$python manage.py migrate</p>
    <p>$python manage.py createsuperuser</p>





