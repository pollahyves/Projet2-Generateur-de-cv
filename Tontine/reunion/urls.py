from django.urls import path
from reunion.views import *


urlpatterns = [
    path('',Login,name='Login'),
    path('register',register,name='register'),
    path('home',home,name='home'),
    path('structure',structure,name='structure'),
    path('actifs_f',actifs_f,name='actifs_f'),
    path('candidat_s',candidat_s,name='candidat_s'),
    path('cotisation_f',cotisation_f,name='cotisation_f'),
    path('election_s',election_s,name='election_s'),
    path('finance',finance,name='finance'),
    path('fonds_f',fonds_f,name='fonds_f'),
    path('membre_s',membre_s,name='membre_s'),
    path('pret_f',pret_f,name='pret_f'),
    path('rapport',rapport,name='rapport'),
    path('register',register,name='register'),
    path('reunion_s',reunion_s,name='reunion_s'),
    path('tontine_s',tontine_s,name='tontine_s'),
    
    
]

