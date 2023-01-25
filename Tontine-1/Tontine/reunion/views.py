from django.shortcuts import redirect ,render
from django.contrib.auth import authenticate,login
from reunion.form import UserForm, RowTontineForm,RowFondForm,ReunionCreationForm,ParticipeForm
from .models import *
from django.views.generic import ListView
from django.db.models import Q
from django.contrib import messages
from django.db import connection

# Create your views here.


#la fonction qui va savoir ou nous envoyer a partir du login
def Login(request):
    error = ''
    a=""
    if request.method == 'POST':
        #on recupere le password et le username de lutilisateur
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:#si lutilisateur exist
            login(request,user)
           
            return redirect('home')
                        
        else:
            error = "password or username incorect" 
               
    return render(request,'login.html',{'error':error})

def register(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
         
    return render(request,'register.html',{'form':form})        

    

def structure(request):
    return render(request,'structure.html')

def actifs_f(request):
    return render(request,'actifs_f.html')
    
def candidat_s(request):
    return render(request,'candidat_s.html')

def home(request):
    return render(request,'home.html')

def election_s(request):
    return render(request,'election_s.html') 

def finance(request):
    return render(request,'finance.html') 

def fonds_f(request):
    return render(request,'fonds_f.html') 

def membre_s(request):
    return render(request,'membre_s.html') 

def pret_f(request):
    return render(request,'pret_f.html') 

def rapport(request):
    return render(request,'rapport.html') 

def reunion_s(request):
    return render(request,'reunion_s.html') 

def tontine_s(request):
    return render(request,'tontine_s.html') 

def cotisation_f(request):
    return render(request,'cotisation_f.html') 



def TontineCreate(request):
     
    form = RowTontineForm()
    user = request.user
    if request.method == 'POST':
        form = RowTontineForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            new = Tontine.objects.create(**form.cleaned_data)
            new.save()
            messages.success(request, f'La tontine a bien ete cree')
            return redirect('/tontine/gestion de la tontine')
        else:
            form = RowTontineForm(request.POST)
    return render(request, 'tontine/create.html', {'form':form, 'user':user})

def tontine(request):
    context = {
        'tontines': Tontine.objects.all()
    }
    return render(request, 'tontine/gestion_de_la_tontine.html', context)


def TontineModify(request, pk):
    obj = Tontine.objects.get(id_tontine=pk)

    form = RowTontineForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        messages.success(request, f'La modification a ete effectue')
        return redirect('/tontine/gestion de la tontine')

    return render(request, 'tontine/update.html', {'form':form})

def TontineDelete(request, pk):
    item = Tontine.objects.get(id_tontine=pk)
    item.delete()
    messages.success(request, f'La tontine a bien ete supprime')
    return redirect('/tontine/gestion de la tontine')

class TontineSearch(ListView):
    model = Tontine
    template_name = 'tontine/search_tontine.html'
    context_object_name = 'tontines'

    def get_queryset(self):
        query = self.request.GET.get('query')
        tontines=Tontine.objects.filter(Q(nom__icontains=query))
        return tontines

def DefinirFond(request):
    
    form = RowFondForm()
    user = request.user
    if request.method == 'POST':
        form = RowFondForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            new = Fond.objects.create(**form.cleaned_data)
            new.save() 
            messages.success(request, f'Le fond a ete definir')
            return redirect('/fond/gestion des fond')
        else:
            form = RowFondForm(request.POST)
    return render(request, 'fond/create.html',{'form':form, 'user':user})  

def fond(request):
   
    context = {
        'fonds': Fond.objects.all(),
      
    }
    
    return render(request, 'fond/gestion_des_fond.html', context)     

def ModifyFond(request, pk):
    obj = Fond.objects.get(id_fond=pk)

    form = RowFondForm(request.POST or None, instance=obj)

    if form.is_valid():
        
        form.save()
        messages.success(request, f'La modification a ete effectue')
        return redirect('/fond/gestion des fond')

    return render(request, 'fond/update.html', {'form':form})

def DeleteFond(request, pk):
    item = Fond.objects.get(id_fond=pk)
    item.delete()
    messages.success(request, f'Le fonds ete supprime')
    return redirect('/fond/gestion des fond')

class FondSearch(ListView):
    model = Fond
    template_name = 'fond/search_fond.html'
    context_object_name = 'fonds'

    def get_queryset(self):
        query = self.request.GET.get('query')
        fonds=Fond.objects.filter(Q(nom_fond__icontains=query))
        return fonds

def create_reunion(request):
    template = 'tontine/create_reunion.html'
    context = {}

    if request.user.is_authenticated:
        if request.method == 'POST':
            reunion = ReunionCreationForm(request.POST or None)
            if reunion.is_valid():
                reunion.save()
                return redirect('reunion_s')
    tontine = ReunionCreationForm()

    context['form'] = tontine

    return render(request, template, context)
    
def mes_reunion(request):
    template = 'tontine/mes_reunion.html'
    
    print("===============================================")

    users = Tontine.objects.all()
    ton =Reunion.objects.all()
    # print(users)
    # l = []

    # for u in users:
    #     meston = MesReunion.objects.filter(membre=u.id_membre)
    #     l.append(meston)
       
    context={
        'result':users,
        'tonti':ton
    }

    return render(request, template, context)            

# # AFFICHIER LES DIFFERENTE REUNION D"UNE ASSOCIATION


# def list_reunion(request, id):
#     template = 'tontine/reunion_tontine.html'
#     return


def info_reunion(request):

    reunion = Reunion.objects.all()
    context={
    'reunions':reunion
    }

    return render(request, 'reunion/info_reunion.html', context)

def Participe_R(request):
     
    form = ParticipeForm()
    user = request.user
    if request.method == 'POST':
        form = ParticipeForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            new = ListePresence.objects.create(**form.cleaned_data)
            new.save()
            # messages.success(request, f'La tontine a bien ete cree')
            return redirect('/reunion_s')
        else:
            form = ParticipeForm(request.POST)
    return render(request, 'reunion/participeR.html', {'form':form, 'user':user})