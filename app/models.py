from __future__ import unicode_literals
from django.db import models
from django.contrib import admin

class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length = 30)
    password = models.CharField(max_length = 30)
    def __unicode__(self):
        return self.username

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','password')

