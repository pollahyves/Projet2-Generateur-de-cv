from django.shortcuts import redirect ,render
from django.contrib.auth import authenticate,login
from reunion.form import UserForm 

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
            # if user.is_comissaire:
            #     return redirect('comissaire')
            # elif user.is_president:
            #     return redirect('president')
            # elif user.is_secretaire:
            #     return redirect('secretaire')
            # else:
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
