from django.shortcuts import redirect ,render
from django.contrib.auth import authenticate,login
from reunion.form import UserForm 

# Create your views here.


#la fonction qui va savoir ou nous envoyer a partir du login
def home(request):
    error = ''
    if request.method == 'POST':
        #on recupere le password et le username de lutilisateur
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:#si lutilisateur exist
            login(request,user)
            if user.is_comissaire:
                return redirect('comissaire')
            elif user.is_president:
                return redirect('president')
            elif user.is_secretaire:
                return redirect('secretaire')
            else:
                return redirect('membre')            
        else:
            error = "password or username incorect" 
    return render(request,'login.html',{'error':error})

def register(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'register.html',{'form':form})        

    

def president(request):
    return render(request,'president.html')

def secretaire(request):
    return render(request,'secretaire.html')
    
def comissaire(request):
    return render(request,'comissaire_aux_compte.html')

def membre(request):
    return render(request,'membre.html')                        