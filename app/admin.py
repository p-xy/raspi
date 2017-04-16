from django.contrib import admin
from .models import User,UserAdmin

# Register your models here.
admin.site.register(User,UserAdmin)