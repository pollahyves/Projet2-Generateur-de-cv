from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Membre


class UserForm(UserCreationForm):
    class Meta:
        model = Membre
        fields = ['username','prenom','e_mail','adresse',
        'telephone','date_naissance','profession',
         'password1', 'password2']
       