from django import forms
from .models import Autor, Libro
from django.contrib.auth.models import User


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'descripcion', 'editorial', 'paginas', 'autor']


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'apellidos', 'nacionalidad']


class BuscarForm(forms.Form):
    query = forms.CharField(label='Busqueda', max_length=100)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
