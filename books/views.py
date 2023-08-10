from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

from .forms import LibroForm, AutorForm, BuscarForm
from .models import Libro, Autor


def index(request):
    libros = Libro.objects.all()
    limite = 5
    paginator = Paginator(libros, limite)
    page_number = request.GET.get('page')
    paginas = paginator.get_page(page_number)
    return render(request, './libros.html', {'libros': libros, 'paginas': paginas})


def books(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    return render(request, './detalles_libro.html', {'libro': libro})


def autores(request):
    autores = Autor.objects.all()
    limite = 5
    paginator = Paginator(autores, limite)
    page_number = request.GET.get('page')
    paginas = paginator.get_page(page_number)
    return render(request, 'autores.html', {'autores': autores, 'paginas': paginas})


def detalles_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    print(autor)
    return render(request, './detalle_autores.html', {'autor': autor})


def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro Creado')
            return redirect('crear_libro')
    else:
        form = LibroForm()

    return render(request, './crear_libro.html', {'form': form}, )


def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor Creado')
            return redirect('crear_autor')
    else:
        form = AutorForm()

    return render(request, './crear_autores.html', {'form': form}, )


def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == 'POST':
        libro.delete()
        messages.success(request, 'Libro Eliminado')
        return redirect('index')
    return render(request, './eliminar_libro.html', {'libro': libro})


def eliminar_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    if request.method == 'POST':
        autor.delete()
        messages.success(request, 'Autor Eliminado')
        return redirect('autores')
    return render(request, './eliminar_autor.html', {'autor': autor})


def editar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro editado')
            return redirect('books', libro_id=libro.id)
    else:
        form = LibroForm(instance=libro)

    return render(request, './editar_libro.html', {'form': form, 'libro': libro})


def editar_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor editado')
            return redirect('detalles_autor', autor_id=autor.id)
    else:
        form = AutorForm(instance=autor)

    return render(request, './editar_autor.html', {'form': form, 'autor': autor})


def buscar(request):
    query = request.GET.get('query')
    form = BuscarForm
    if query:
        libros = Libro.objects.filter(titulo__icontains=query) | Libro.objects.filter(
            autor__nombre__icontains=query) | Libro.objects.filter(editorial__icontains=query)
        autores = Autor.objects.filter(nombre__icontains=query) | Autor.objects.filter(apellidos__icontains=query)
    else:
        libros = []
        autores = []

    return render(request, './busqueda.html', {'query': query, 'libros': libros, 'autores': autores, 'form': form})


class UserFormView(View):
    form_class = UserForm
    template_name = './registro.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('index')
        return render(request, self.template_name, {'form': form})
