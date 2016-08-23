from django.contrib import admin
from .models import UserData

class UserDataAdmin(admin.ModelAdmin):
    model = UserData
    list_display = ['first_name', 'last_name', 'age', 'gender', 'address']


admin.site.register(UserData, UserDataAdmin)