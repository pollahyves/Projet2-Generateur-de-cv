from django.contrib import admin
from .models import CreateBlog,Comment

# Register your models here.

# on va enregistrer les 2 sur forme de table dans le admin donc c'est pour sa que nous allons cree une class
class BlogAdmin(admin.ModelAdmin):
    list_display=('title','intro','slug','date_added')

class CommentAdmin(admin.ModelAdmin):
    list_display=('body','email','date_added')    

# enregistrement des model
admin.site.register(CreateBlog,BlogAdmin)
admin.site.register(Comment,CommentAdmin)    