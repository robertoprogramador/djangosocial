#from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
class Perfil(models.Model):
    usuario = models.CharField(max_length=255)
    #author = models.foreignKey(User, on_delate=models.CASCADE)
    cidade = models.CharField(max_length=50, default="saopaulo")
    sexo = models.CharField(max_length=1)
    slug = models.SlugField(max_length=255, unique=True)
    sobre = models.TextField()
    danca = models.CharField(max_length=2)
    viagem = models.CharField(max_length=2)
    cozinhar = models.CharField(max_length=2)
    filmes = models.CharField(max_length=2)
    barzinhos = models.CharField(max_length=2)
    shows = models.CharField(max_length=2)
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media')#, blank=True
    list_filter=['sexo']
    search_fields=['cidade']
    objects = models.Manager()
    
    def __str__(self):
        return self.usuario 

    def get_absolute_url(self):
        return reverse("perfis:detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ("-created",)

#list_filter=['sexo']
#search_fields=['cidade']
