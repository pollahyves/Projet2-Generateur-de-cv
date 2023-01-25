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
    path('tontine/create', TontineCreate, name='create_tontine' ),
    path('tontine/gestion de la tontine', tontine, name='gestion_tontine'),
    path('tontine/update/<int:pk>', TontineModify, name='update_tontine'),
    path('tontine/delete/<int:pk>', TontineDelete, name='delete_tontine'),
    path('tontine/search', TontineSearch.as_view(), name='search_tontine'),
    path('fond/create', DefinirFond, name='create_fond' ),
    path('fond/gestion des fond',fond, name='gestion_fond'),
    path('fond/update/<int:pk>', ModifyFond, name='update_fond'),
    path('fond/delete/<int:pk>', DeleteFond, name='delete_fond'),
    path('fond/search', FondSearch.as_view(), name='search_fond'),
    path('mes_reunion/', mes_reunion, name='mes_reunion'),
    path('creation_reunion/', create_reunion, name="create_reunion"),
    path('reunions/reunion', Participe_R, name='Preunion'),
    path('reunions/info_reunion', info_reunion, name='info_reunion'),
    
]

