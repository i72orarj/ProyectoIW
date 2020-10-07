from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Categoria(models.Model):
    nombre=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Videojuego(models.Model):
    nombre=models.CharField(max_length=100)
    fechaLanzamiento=models.IntegerField()
    descripcion=models.CharField(max_length=1000)
    # categoria=models.CharField(max_length=100,blank=True, null=True)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    portada=models.CharField(max_length=100)
    numeroJugadores=models.IntegerField()

    def __str__(self):
        return self.nombre  

class EnlaceCompra(models.Model):
    videojuego=models.ForeignKey(Videojuego,on_delete=models.CASCADE)
    tienda=models.CharField(max_length=100)
    enlace=models.CharField(max_length=1000)

    def __str__(self):
        return self.videojuego.nombre + " " + self.tienda

class Trailer(models.Model):
    videojuego=models.ForeignKey(Videojuego,on_delete=models.CASCADE)
    enlace=models.CharField(max_length=1000)

    def __str__(self):
        return str(self.id) + " " + self.videojuego.nombre

class Critica(models.Model):
    videojuego = models.ForeignKey(Videojuego, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=5000)
    nota = models.IntegerField()
    criticaRespondida = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + self.videojuego.nombre + " " +  self.autor.username

class Valoracion(models.Model):
    critica = models.ForeignKey(Critica,on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    valor = models.BooleanField()

    def __str__(self):
        return self.critica.videojuego.nombre + " " + str(self.critica.id) + " " + self.autor.username

