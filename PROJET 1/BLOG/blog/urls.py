from django.urls import path
from blog.views import *

urlpatterns = [
    path('',List.as_view(),name ="home"),
]