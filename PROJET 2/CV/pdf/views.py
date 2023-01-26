from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import Profile
from .form import ProfileForm
#on va import ceci pour la generation du pdf
import pdfkit
from django.template.loader import get_template
import io

# Create your views here.

def index(request):
    return render(request,'pdf/resume.html')

#fonction pour enregistrer les information entrer dans le formulaire dans la base de donees
def formulaire(request):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(data = request.POST)
        form.save()
        form = ProfileForm()
        return redirect('verification')
    return render(request,'pdf/form.html',{'form':form})

#fonction pour ramener le premier element de la bd et afficher
def verification(request):
    profile = Profile.objects.all()[:1]  #[:1] cest pour prendre le premier element puisque le all nous renvois tout les element de la bd

    for prof in profile:
        name = prof.name
        email = prof.email
        phone = prof.phone
        address =prof.address
        langue = prof.langue
        competance = prof.competance 
        interet = prof.interet
        objectif = prof.objectif
        experience = prof.experience
        education = prof.experience
        Projet = prof.Projet

    return render(request,'pdf/verification.html',{'name':name,'email':email,'phone':phone,'address':address,'langue':langue,'competance':competance,'interet':interet,'objectif':objectif,'experiance':experience,'education':education,'projet':Projet})   

#fonction pour generer le pdf du CV
def generator(request,id):
    prof = Profile.objects.get(pk=id)
    name = prof.name
    email = prof.email
    phone = prof.phone
    address =prof.address
    langue = prof.langue
    competance = prof.competance 
    interet = prof.interet
    objectif = prof.objectif
    experience = prof.experience
    education = prof.experience
    Projet = prof.Projet

    template = get_template('pdf/generator.html')

    context = {'name':name,'email':email,'phone':phone,'address':address,'langue':langue,'competance':competance,'interet':interet,'objectif':objectif,'experiance':experience,'education':education,'projet':Projet}
     
    html = template.render(context) 
    options = {
        'page-size':'Letter', # la taille de la page doit etre comme pour une lettre
        'encoding':'UTF-8',
    }

    pdf = pdfkit.from_string(html, False,options)

    reponse = HttpResponse(pdf,content_type='application/pdf')
    # pour telecharcher le pdf
    reponse['Content-Disposition'] = "attachement"

    return reponse

 #fonction pour telecharche le CV en pdf
def download(request):
    profile = Profile.objects.all()
    return render(request,'pdf/download.html',{'profile':profile})
