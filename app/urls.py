from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^login$',views.login),
	url(r'^logout$',views.logout),
	url(r'^$',views.index),
	url(r'^look$',views.look),
	url(r'^control$',views.control),
]
