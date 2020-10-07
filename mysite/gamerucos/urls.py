from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name="login"),
    path('registro', views.registro, name="registro"),
    path('buscar', views.buscar, name="buscar"),
    path('comprobarTitulo', views.buscarTituloForm, name='buscarTituloForm'),
    path('comprobarCategoria', views.buscarCategoriaForm, name='buscarCategoriaForm'),
    path('videojuegos/titulo/<str:titulo>', views.videojuegosTitulo, name='videojuegosTitulo'),
    path('videojuegos/categoria/<str:categoria>', views.videojuegosCategoria, name='videojuegosCategoria'),
    path('comentar/<int:idVideojuego>', views.comentarVideojuego, name="comentarVideojuego"),
    path('comentar/<int:idVideojuego>/<int:idCritica>', views.comentarCritica, name="comentarCritica"),
    path('acerca', views.acerca, name="acerca"),
    # path('videojuegos',views.videojuegos,name="videojuegos"),
    path('recomendaciones', views.recomendaciones, name='recomendaciones'),
    path('comprobarLogin', views.loginForm, name='loginForm'),
    path('comprobarRegistro', views.registroForm, name='registroForm'),
    path('comprobarCritica', views.comprobarCritica ,name='comprobarCritica'),
    path('comprobarRespuesta', views.comprobarRespuesta ,name='comprobarRespuesta'),
    path('valorarPositivo/<int:idVideojuego>/<int:idCritica>', views.valorarPositivo, name='valorarPositivo'),
    path('valorarNegativo/<int:idVideojuego>/<int:idCritica>', views.valorarNegativo, name='valorarNegativo'),
    path('videojuegos/<int:idVideojuego>', views.videojuego, name='videojuego'),
    path('perfil', views.miPerfil, name='miPerfil'),
    path('perfil/<int:idUsuario>', views.perfil, name='perfil'),
    path('logout', views.logout, name='logout'),
]
