from django import forms

class contactoForm(forms.Form):
    nombre = forms.CharField( label='Nombre',max_length=100, required=True)
    telefono = forms.CharField(label='Telefono de contacto',max_length='30',required=True)
    fechanacimiento = forms.DateField(label='Fecha de Nacimiento',required=True)
    numerodepie = forms.IntegerField(label='Numero de Pie', required=False)