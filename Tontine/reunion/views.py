from django.shortcuts import redirect ,render
from django.contrib.auth import authenticate,login

# Create your views here.


#la fonction qui va savoir ou nous envoyer a partir du login
def home(request):
    error = ''
    if request.method == 'POST':
        #on recupere le password et le username de lutilisateur
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:#si lutilisateur exist
            login(request,user)
            if user.is_comissaire:
                return redirect('commisaire_aux_compte')
            elif user.is_president:
                return redirect('president')
            elif user.is_secretaire:
                return redirect('secretaire')
            else:
                return redirect('membre')            
        else:
            error = "password or username incorect" 
    return render(request,'login.html',{'error':error})        