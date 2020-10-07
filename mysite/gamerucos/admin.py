from django.contrib import admin

# Register your models here.

from .models import Videojuego,Critica,EnlaceCompra,Trailer,Valoracion,Categoria

admin.site.register(Videojuego)
admin.site.register(Critica)
admin.site.register(EnlaceCompra)
admin.site.register(Trailer)
admin.site.register(Valoracion)
admin.site.register(Categoria)