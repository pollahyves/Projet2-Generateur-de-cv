from django.contrib import admin
from .models import Profile

# Register your models here.

class AdminProfile(admin.ModelAdmin):
    list_display=['name','email','phone','address','langue']

admin.site.register(Profile,AdminProfile)
