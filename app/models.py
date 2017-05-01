from __future__ import unicode_literals
from django.db import models
from django.contrib import admin

class LED_FORM(models.Model):
    switch = models.CharField(max_length=30)
    id = models.IntegerField(primary_key=True,max_length=30)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','switch')

