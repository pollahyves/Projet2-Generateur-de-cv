from django.urls import path
from blog.views import *

urlpatterns = [
    path('home',List.as_view(),name ="home"),
    path('detail/<slug:slug>',detailleView,name='detailView')
]