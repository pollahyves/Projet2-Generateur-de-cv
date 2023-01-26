from django import forms
from django.forms import ModelForm
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
       

        widgets = {
    
    'name':forms.TextInput(attrs={'placeholder': 'nom et prenom', 'style': 'width: 600px;', 'class': 'form-control'}),
    'email':forms.EmailInput(attrs={'placeholder': 'example:yvesfranky961@gmail.com', 'style': 'width: 600px;', 'class': 'form-control'}),
    'phone':forms.TextInput(attrs={'placeholder': '+237678654432', 'style': 'width: 600px;', 'class': 'form-control'}),
    'address':forms.TextInput(attrs={'placeholder': 'cameroun yaounde essomba', 'style': 'width: 600px;', 'class': 'form-control'}),
    'competance':forms.TextInput(attrs={'placeholder': 'python,django,java,c++', 'style': 'width: 600px;', 'class': 'form-control'}),
    'interet':forms.TextInput(attrs={'placeholder': 'football,programmation,lecture', 'style': 'width: 600px;', 'class': 'form-control'}),
    'objectif' :forms.Textarea(attrs={'placeholder': 'votre objecif ici', 'style': 'width: 600px;', 'class': 'form-control', 'rows':5, 'cols':10}),
    'experiance' :forms.Textarea(attrs={'placeholder': 'votre experiance ici,precisez le poste,lentrprise et la duree', 'style': 'width: 600px;', 'class': 'form-control', 'rows':5, 'cols':10}),
    'education' :forms.Textarea(attrs={'placeholder': 'Baccaluareat C 2021 lycee bilingue de paris', 'style': 'width: 600px;', 'class': 'form-control', 'rows':5, 'cols':10}),
    'Projet' :forms.Textarea(attrs={'placeholder': 'jai developer de blog pour un salon de coiffure.pour presenter les differant style de coiffure et entrer en contact avec le coiffeur.mon code est sur gitup.contacter moi pour avoir mon lien', 'style': 'width: 600px;', 'class': 'form-control', 'rows':5, 'cols':10}),
    'langue':forms.TextInput(attrs={'placeholder': 'francais,anglais,chinois', 'style': 'width: 600px;', 'class': 'form-control'}),

    } 
