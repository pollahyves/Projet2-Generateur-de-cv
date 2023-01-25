from django.shortcuts import render,redirect
from django.views.generic import ListView
from .models import CreateBlog
from .forms import BlogForm

# Create your views here.
# on va utiliser la paggination pour les page 
# sur notre site donc on va utiliser les class pour envoyer notre templates a l'ecran

class List(ListView):
    template_name = 'blog/index.html'
    queryset = CreateBlog.objects.all() # je recupere tout les object du tableau Createblog    
    paginate_by = 2 #cest pour avoir 2 poste par page

# pour avoir le detaile sur une article en fonction du slog
def detailleView(request, slug):
    post = CreateBlog.objects.get(slug=slug)    # ici on recupere l'article grace au slug
    # on veut relier chaque commentaire a un article
    comments = post.comments.all() # le comments qui est au milieu de post et all cest le related name dans le model Comment
    
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save(commit=False)# le commit=False parce que dans notre formulaire on ne recupere pa tout les element de la bade de donnees
            form.instance.post = post #pour dire le post que il va enregistrer sera le post lie a larticle si
            form.save()
            return redirect('detailView',slug=post.slug)
        
    else:
        form = BlogForm()    
    content = {
        'article':post,
        'comments':comments, # puisque nous aurons besoin d'afficher tout les commentaire
        'form':form # on a ausi besoin d'envoyer le formulaire ver le template
     }


    return render(request,'blog/update.html',content)