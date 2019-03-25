from django.contrib import admin
from .models import *
# Register your models here.
class UserinfoAdmin(admin.ModelAdmin):
    list_display = ['username','password']
    list_display_links = ['username']
admin.site.register(UserInfo,UserinfoAdmin)