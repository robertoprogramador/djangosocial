#from django.shortcuts import render

from django.views.generic import DetailView,ListView

from .models import Perfil

class PerfilListview(ListView):
    model = Perfil

class PerfilDetailview(DetailView):
    model = Perfil 

