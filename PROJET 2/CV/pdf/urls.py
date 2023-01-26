from django.urls import path
from pdf.views import *

urlpatterns = [

    path('',index,name ='acceuil'),
    path('creercv',formulaire,name="creer"),
    path('verification',verification,name='verification'),  
    path('<int:id>',generator,name='generator'),
    path('download',download,name = 'download')                   
]