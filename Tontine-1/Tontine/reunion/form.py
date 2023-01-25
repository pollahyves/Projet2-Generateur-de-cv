from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Membre, Tontine,Fond,Reunion,ListePresence


class UserForm(UserCreationForm):
    class Meta:
        model = Membre
        fields = ['username','prenom','e_mail','adresse',
        'telephone','date_naissance','profession',
         'password1', 'password2']

        widget ={
'date_naissance':forms.DateInput(attrs={'type':'date'})
         }
    
class RowTontineForm(forms.ModelForm):
    nom = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Entrer le nom', 'style': 'width: 600px;', 'class': 'form-control'}))
    date_creation = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'Entrer la date de création', 'style': 'width: 600px;', 'class': 'form-control'}))
    slogan = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'placeholder': 'Entrer le slogan', 'style': 'width: 600px;', 'class': 'form-control'}))
    regle = forms.CharField(max_length=250, required=False, widget=forms.Textarea(attrs={'placeholder': 'Entrer le(s) regle(s)', 'style': 'width: 600px;', 'class': 'form-control', 'rows':5, 'cols':10}))
    author = forms.CharField(max_length=25)

    class Meta:
        model = Tontine
        fields = ['nom','date_creation','slogan','regle']
 

      

class RowFondForm(forms.ModelForm):
    objectif=forms.Textarea

    class Meta:
        model = Fond
        fields = '__all__'
       

        widgets = {
    # 'id_fond': forms.IntegerField(max_value=30 ,required=False),
    'id_tontine':forms.Select(attrs={'placeholder': 'Choisir ton id', 'style': 'width: 600px;', 'class': 'form-control'}),
    'id_membre': forms.NumberInput(attrs={'value':'','style': 'width: 600px;', 'class': 'form-control','id':'idm','type':'hidden'}),
    'type_fond': forms.TextInput(attrs={'placeholder': 'Entrer le type de fond', 'style': 'width: 600px;', 'class': 'form-control'}),
    'nom_fond': forms.TextInput(attrs={'placeholder': 'Entrer le nom du fond', 'style': 'width: 600px;', 'class': 'form-control'}),
    'montant': forms.NumberInput(attrs={'placeholder': 'Entrer le montant du fond', 'style': 'width: 600px;', 'class': 'form-control'}),
    'objectif' :forms.Textarea(attrs={'placeholder': 'Entrer le(s) objective du fond', 'style': 'width: 600px;', 'class': 'form-control', 'rows':5, 'cols':10}),
    'author':forms.CharField(max_length=25)

    }  

class ReunionCreationForm(ModelForm):

    class Meta:
        model = Reunion
        fields = '__all__'
        #fields = ['tontine', 'nom', 'date', 'motif', 'lieu', 'heure']


class ParticipeForm(forms.ModelForm):
    class Meta:
        model = ListePresence
        fields = '__all__'

        widgets = {
    
    'id_tontine':forms.Select(attrs={'placeholder': 'Choisir ton id', 'style': 'width: 600px;', 'class': 'form-control'}),
    'id_membre': forms.NumberInput(attrs={'value':'','style': 'width: 600px;', 'class': 'form-control','id':'idm','type':'hidden'}),    
        }