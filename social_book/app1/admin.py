from django.contrib import admin
from .models import CustomUser
# Register your models here.


@admin.register(CustomUser)

class CustomUser_Admin(admin.ModelAdmin):
    list_display=('email','first_name','last_name','gender','public_visibility')