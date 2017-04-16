from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length = 30)
    password = models.CharField(max_length = 30)


class UserAdmin(admin.ModelAdmin):
    list_display = ('email','password')
