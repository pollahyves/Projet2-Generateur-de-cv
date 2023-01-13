from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth import get_user_model
from .models import Membre

# Membre = get_user_model()
class UserForm(UserCreationForm):
    class Meta:
        model = Membre
        fields = ['username','prenom','e_mail','adresse','telephone','date_naissance','profession', 'password1', 'password2']
        # fields=[
        #     'username',
        #     'password1',
        #     'password2'
        # ]