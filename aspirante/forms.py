from django import forms

class registrarAspirante(forms.Form):
    nombres = forms.CharField(label='Nombres', required=True, widget=forms.TextInput(attrs={"autofocus": True}))
    apellidos = forms.CharField(label='Apellidos', required=True)
    numeroDocumento = forms.CharField(label='Documento', max_length=15, required=True)
    tipoDocumento = forms.CharField("Tipo documento", max_length=5, required=True)
    profesion = forms.CharField("profesion", max_length=10, required=True)
    edad = forms.IntegerField("edad", required=True)
    ciudad = forms.CharField("ciudad", max_length=20, required=True)