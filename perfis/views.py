#from django.shortcuts import render

from django.views.generic import DetailView,ListView

from .models import Perfil


class PerfilListview(ListView):
    model = Perfil
    #template_name="perfil_list.html"
    def get_queryset(self):
        return Perfil.objects.order_by('cidade')
    def get_queryset(self):
        txt_nome = self.request.GET.get('cidade')
        txt_nome2 = self.request.GET.get('sexo')
        
        
        if txt_nome and txt_nome2 :
            meufiltro = Perfil.objects.filter(cidade=txt_nome, sexo=txt_nome2)
           
            
        else:
            meufiltro = Perfil.objects.all()

        return meufiltro
        

class PerfilDetailview(DetailView):
    model = Perfil 

