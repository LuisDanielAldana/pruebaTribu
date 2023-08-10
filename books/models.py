from django.db import models


class Autor(models.Model):
    nombre = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=500)
    nacionalidad = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre + ' - ' + self.apellidos + ' - ' + self.nacionalidad


class Libro(models.Model):
    titulo = models.CharField(max_length=250)
    descripcion = models.CharField(max_length=250)
    editorial = models.CharField(max_length=250)
    paginas = models.IntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo + ' - '
