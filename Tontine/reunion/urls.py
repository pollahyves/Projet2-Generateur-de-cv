from django.urls import path
from reunion.views import register,home,comissaire,secretaire,membre,president
from reunion.models import Candidat

urlpatterns = [
    path('',home,name='home'),
    path('register',register,name='register'),
    path('membre',membre,name='membre'),
    path('president',president,name='president'),
    path('comissaire',comissaire,name='comissaire'),
    path('secretaire',secretaire,name='secretaire'),
    
]

