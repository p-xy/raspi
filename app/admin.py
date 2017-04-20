from django.contrib import admin
from .models import User,UserAdmin

admin.site.register(User,UserAdmin)
