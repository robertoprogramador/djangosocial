from django.contrib import admin

from .models import (Perfil)

#admin.site.register(Perfil)

# Register your models here.
@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ("usuario", "cidade", "sexo", "created", "updated")
    prepopulated_fields = {"slug": ("usuario",)}