from django.conf.urls import url

from . import views



urlpatterns = [
	url(r'^$',views.login),
	url(r'^LED_switch/$',views.LED_switch)
]
