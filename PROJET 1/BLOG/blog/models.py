from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
# nous alons cree notre base de donnes ici

class CreateBlog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()# c'est un identifiant pour chaque article dans le lien
    intro = models.TextField() # chaque article a un introduction
    body = models.TextField() # le corps de larticle
    image = models.ImageField(upload_to='media')# chaque article aura une image .media c'est lendroit ou les image vont etre stocker
    date_added = models.DateTimeField(auto_now=True)# la date et l'heur auquel larticle a ete ajouter
    # auto_now=True cest pour que lorseque je publie un article,sa mets la date et l'heur de l'instant la

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-date_added'] # qui signifie que les date recente seron en haut c'est a dire que les article seront vut en ordre de publication

# class des commentaire sur les article
class Comment(models.Model):
    post = ForeignKey(CreateBlog,related_name = 'comments',on_delete=models.CASCADE) # chaque commentaire doit etre lie a un article
    # on_delete=models.CASCADE pour que si on suprime les commentaire d'un article,sa ne joue pa sur larticle
    email = models.EmailField()
    body= models.TextField()
    name = models.CharField(max_length=200,default="inconnu")#le nom de la personne qui fait le commentaire par defaut cest un inconnu
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_added']