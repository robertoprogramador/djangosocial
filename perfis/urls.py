from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "perfis"

urlpatterns = [
    path("", views.PerfilListview.as_view(), name="list"),
    path("<slug:slug>/", views.PerfilDetailview.as_view(), name="detail"),
     ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#(r'^_media/(?P<path>.*)$', 'django.views.static.serve',
#{'document_root': '/path/to/media'}),