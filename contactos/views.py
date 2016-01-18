from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from contactos.models import Contacto
from django.forms import modelform_factory
from django.contrib import messages


def eliminarcontacto (request, id_contacto):
    contacto = get_object_or_404(Contacto, pk=id_contacto)
    messages.add_message(request, messages.SUCCESS,'Contacto Eliminado Correctamente')
    contacto.delete()
    return HttpResponseRedirect(reverse('contactos:ver') )


def editarcontacto(request, id_contacto=None):
    es_modificacion =(id_contacto!=None)
    contactoForm =modelform_factory(Contacto,exclude=())
    if es_modificacion:
        contacto = get_object_or_404(Contacto, id=id_contacto)
    else:
        contacto=Contacto()

    if request.method == 'POST':
        form = contactoForm(request.POST,instance=contacto)
        if form.is_valid():
            contacto = form.save()
            messages.add_message(request, messages.SUCCESS, 'Su contacto ha sido modificado')
            return HttpResponseRedirect(reverse('contactos:ver'))
        else:
            messages.add_message(request, messages.ERROR, 'Los datos que has introducido no son correctos')
    else:
        form = contactoForm(instance=contacto)
    return render(request, 'contactos/formulario.html', {'form': form, 'titol':"Formulario",'h1':"Foromulario",'contacto':contacto,'botton':"Editar"})

def vercontactos(request):
    contactos = Contacto.objects.all()
    return render(request, 'contactos/index.html', {'contactos': contactos})

#from .forms import contactoForm

# def entrarcontacto(request):
#     if request.method == 'POST':
#         form = contactoForm(request.POST)
#         if form.is_valid():
#             Contacto.objects.create(nombre=form.cleaned_data['nombre'],
#                                     telefono=form.cleaned_data['telefono'],
#                                     fechanacimiento=form.cleaned_data['fechanacimiento'],
#                                     numerodepie=form.cleaned_data['numerodepie'])
#             messages.add_message(request, messages.INFO, 'Su nuevo contacto ha sido creado correctamente')
#             return HttpResponseRedirect(reverse('contactos:ver'))
#         else:
#             messages.add_message(request, messages.ERROR, 'Los datos que has introducido no son correctos')
#     else:
#         form = contactoForm()
#     return render(request, 'contactos/formulario.html', {'form': form, 'titol':"Formulario",'h1':"Formulario"})


# def editarcontacto(request, id_contacto):
#
#     contacto = get_object_or_404(Contacto, id=id_contacto)
#
#     if request.method == 'POST':
#         form = contactoForm(request.POST)
#         if form.is_valid():
#             contacto.nombre=form.cleaned_data['nombre']
#             contacto.telefono=form.cleaned_data['telefono']
#             contacto.fechanacimiento=form.cleaned_data['fechanacimiento']
#             contacto.numerodepie=form.cleaned_data['numerodepie']
#             contacto.save()
#             messages.add_message(request, messages.INFO, 'Su contacto ha sido modificado')
#             return HttpResponseRedirect(reverse('contactos:ver'))
#         else:
#             messages.add_message(request, messages.ERROR, 'Los datos que has introducido no son correctos')
#     else:
#
#         data={'nombre':contacto.nombre,'telefono':contacto.telefono,'fechanacimiento':contacto.fechanacimiento,'numerodepie':contacto.numerodepie}
#         form = contactoForm( initial=data)
#     return render(request, 'contactos/formulario.html', {'form': form, 'titol':"Formulario",'h1':"Foromulario",'contacto':contacto,'botton':"Editar"})




