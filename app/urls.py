#coding=utf-8
from django.conf.urls import url
from . import views
#from . import cp_views as views 


urlpatterns = [
	url(r'^login$',views.login ),
	url(r'^logout$',views.logout),
	url(r'^$',views.index),
	url(r'^look$',views.look),
	url(r'^control$',views.control),
	url(r'^face$',views.face),
	#在本地运行，请注释下面两行
	url(r'^take_a_photo$',views.take_a_photo),
	url(r'^face_compare$',views.face_compare),
	
]
