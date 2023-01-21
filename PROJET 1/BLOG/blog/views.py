from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
# on va utiliser la paggination pour les page 
# sur notre site donc on va utiliser les class pour envoyer notre templates a l'ecran

class List(ListView):
    template_name = '/blog/index.html'