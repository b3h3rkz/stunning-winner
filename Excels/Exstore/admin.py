from django.contrib import admin
from .models import UserData, Log


class UserDataAdmin(admin.ModelAdmin):
    model = UserData
    list_display = ['first_name', 'last_name', 'age', 'gender', 'address']



class LogAdmin(admin.ModelAdmin):
    model = Log
    list_display = ['action', 'message', 'date']




admin.site.register(UserData, UserDataAdmin)
admin.site.register(Log, LogAdmin)