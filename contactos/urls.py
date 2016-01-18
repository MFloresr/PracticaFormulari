from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /contactos/
    url(r'^vercontactos/$', views.vercontactos, name='ver'),
    # ex: /formulario/
    #url(r'^introducircontacto/$', views.entrarcontacto, name='entrar'),
    #ex: /introducircontacto/
    url(r'^introducircontacto/$', views.editarcontacto, name='entrar'),
    url(r'^editarcontactos/(?P<id_contacto>[0-9]+)/$', views.editarcontacto, name='editar'),

    url(r'^eliminarcontactos/(?P<id_contacto>[0-9]+)/$', views.eliminarcontacto, name='eliminar'),
]