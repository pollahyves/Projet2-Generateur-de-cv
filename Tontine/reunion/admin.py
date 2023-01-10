from django.contrib import admin
from .models import User, AppartenirTontine,Candidat,Cotisation,Cotiser,Election,Fond, Membre,ParticipantReunion,Poste,Pret,Reunion,Tontine,Vote


# Register your models here.

admin.site.register(User)
admin.site.register(AppartenirTontine)
admin.site.register(Candidat)
admin.site.register(Cotisation)
admin.site.register(Cotiser)
admin.site.register(Election)
admin.site.register(Fond)
admin.site.register(Membre)
admin.site.register(ParticipantReunion)
admin.site.register(Poste)
admin.site.register(Pret)
admin.site.register(Reunion)
admin.site.register(Tontine)
admin.site.register(Vote)
