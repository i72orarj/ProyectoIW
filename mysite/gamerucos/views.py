from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Videojuego, Critica, EnlaceCompra, Trailer, Valoracion, Categoria
import qrcode
from PIL import Image

def home(request):
    primerVideojuego = Videojuego.objects.get(nombre="Valorant")
    segundoVideojuego = Videojuego.objects.get(nombre="Mortal Kombat 11")
    tercerVideojuego = Videojuego.objects.get(nombre="Fifa 20")
    cuartoVideojuego = Videojuego.objects.get(nombre="Pro Evolution Soccer 20")
    quintoVideojuego = Videojuego.objects.get(nombre="Super Smash Bros Ultimate")
    sextoVideojuego = Videojuego.objects.get(nombre="Fortnite")
    context = {
        'primero':primerVideojuego,
        'segundo':segundoVideojuego,
        'tercero':tercerVideojuego,
        'cuarto':cuartoVideojuego,
        'quinto':quintoVideojuego,
        'sexto':sextoVideojuego,
    }
    if 'idUsuario' in request.session:
        context['logueado'] = 1
    else:
        context['logueado'] = 0
    return render(request, "gamerucos/index.html", context)

def login(request):
    if 'idUsuario' in request.session:
        return redirect('home')
    else:
        return render(request, "gamerucos/login.html")

def loginForm(request):
    usuario = request.POST['user']
    password = request.POST['password']
    user = authenticate(username=usuario, password=password)
    if user is not None:
        request.session['idUsuario'] = user.id
        return redirect('home')
    else:
        return redirect('login')

def registro(request):
    if 'idUsuario' in request.session:
        return redirect('home')
    else:
        return render(request, "gamerucos/registro.html")

def registroForm(request):
    newUser = User.objects.create_user(request.POST['usuario'], request.POST['correo'], request.POST['password'])
    newUser.first_name = request.POST['nombre']
    newUser.last_name = request.POST['apellidos']
    newUser.save()
    user = User.objects.get(username=request.POST['usuario'])
    request.session['idUsuario'] = user.id
    return redirect('home')

def buscar(request):
    categoriasLeidas = Categoria.objects.all()
    if 'idUsuario' in request.session:
        context = {
            'logueado':1,
            'categorias':categoriasLeidas,
        }
    else:
        context = {
            'logueado':0,
            'categorias':categoriasLeidas,
        }

    return render(request, "gamerucos/buscarJuego.html", context)

def buscarTituloForm(request):
    titulo = request.POST['nombreVideojuego']
    return redirect('videojuegosTitulo', titulo=titulo)

def buscarCategoriaForm(request):
    categoria = request.POST['categoriaVideojuego']
    return redirect('videojuegosCategoria', categoria=categoria)

def comentarVideojuego(request, idVideojuego):
    videojuegoLeido = Videojuego.objects.get(id=idVideojuego)
    if 'idUsuario' in request.session:
        context = {
            'logueado':1,
            'videojuego':videojuegoLeido,
        }
    else:
        context = {
            'logueado':0,
            'videojuego':videojuegoLeido,           
        }
    return render(request, "gamerucos/comentar.html", context)

def comprobarCritica(request):
    idVideojuegoCriticado = request.POST['idVideojuego']
    videojuegoCriticado = Videojuego.objects.get(id=idVideojuegoCriticado)
    autor = User.objects.get(id=request.session['idUsuario'])
    nota = request.POST['nota']
    comentario = request.POST['comentario']
    nuevaCritica = Critica.objects.create(videojuego=videojuegoCriticado, autor=autor, comentario=comentario, nota=nota)
    nuevaCritica.save()
    return redirect('home')
    #return redirect('videojuego',idVideojuego=idVideojuegoCriticado)

def comentarCritica(request, idVideojuego, idCritica):
    videojuegoLeido = Videojuego.objects.get(id=idVideojuego)
    criticaLeida = Critica.objects.get(id=idCritica)
    context = {
        'videojuego':videojuegoLeido,
        'critica':criticaLeida,
    }
    if 'idUsuario' in request.session:
        context['logueado'] = 1
    else:
        context['logueado'] = 0
    return render(request, "gamerucos/responder.html", context)

def comprobarRespuesta(request):
    idVideojuegoCriticado = request.POST['idVideojuego']
    videojuegoCriticado = Videojuego.objects.get(id=idVideojuegoCriticado)
    idCriticaRespondida = request.POST['idCritica']
    criticaRespondida = Critica.objects.get(id=idCriticaRespondida)
    autor = User.objects.get(id=request.session['idUsuario'])
    nota = request.POST['nota']
    comentario = request.POST['comentario']
    nuevaCritica = Critica.objects.create(videojuego=videojuegoCriticado, autor=autor, comentario=comentario, nota=nota, criticaRespondida=criticaRespondida)
    nuevaCritica.save()
    return redirect('videojuego', idVideojuego=idVideojuegoCriticado)

def acerca(request):
    if 'idUsuario' in request.session:
        context = {
            'logueado':1,
        }
    else:
        context = {
            'logueado':0,
        }
    return render(request, "gamerucos/acerca.html", context)

def videojuegosTitulo(request, titulo):
    videojuegoLeido = Videojuego.objects.get(nombre=titulo)
    if videojuegoLeido is not None:
        return redirect('videojuego', idVideojuego=videojuegoLeido.id)
    else:
        return redirect('home')

def videojuegosCategoria(request, categoria):
    categoria = Categoria.objects.get(nombre=categoria)
    videojuegosLeidos = Videojuego.objects.all().filter(categoria=categoria)
    context = {
        'videojuegos':videojuegosLeidos,
    }
    if 'idUsuario' in request.session:
        context['logueado'] = 1
    else:
        context['logueado'] = 0
    return render(request, "gamerucos/videojuegos.html", context)

def videojuego(request, idVideojuego):
    if 'idUsuario' not in request.session:
        context = {
            'logueado':0,
            'mensaje':"No está permitido visualizar un videojuego sin estar registrado",
        }
        return render(request, "gamerucos/error.html", context)
    videojuegoLeido = Videojuego.objects.get(id=idVideojuego)
    criticasVideojuegoLeido = Critica.objects.all().filter(videojuego=videojuegoLeido)
    nota = 0
    puntuacionesCriticas = []
    numeroCriticas = 0
    criticas = []
    respuestasCriticas = []
    criticasValoradas = []
    for critica in criticasVideojuegoLeido:
        if critica.criticaRespondida is None:
            criticas.append(critica)
            nota = nota + critica.nota
            numeroCriticas = numeroCriticas + 1
        else:
            respuestasCriticas.append(critica)
        valoraciones = Valoracion.objects.all().filter(critica=critica)
        puntuacion = 0
        for valoracion in valoraciones:
            if valoracion.autor.id == request.session['idUsuario']:
                criticasValoradas.append(critica.id)
            if valoracion.valor == True:
                puntuacion = puntuacion + 1
            else:
                puntuacion = puntuacion - 1
        valoracionCritica = [critica.id, puntuacion]
        puntuacionesCriticas.append(valoracionCritica)
    nota = nota/numeroCriticas
    sitiosVideojuegoLeido = EnlaceCompra.objects.filter(videojuego=videojuegoLeido).all()
    #trailersVideojuegoLeido = Trailer.objects.filter(videojuego=videojuegoLeido).all()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1,
    )
    urlWeb="www.gamerucos.com/videojuegos/"+str(idVideojuego)
    qr.add_data(urlWeb)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    urlQR="gamerucos/static/img/qr.png"
    img.save(urlQR)
    context = {
        'videojuego':videojuegoLeido,
        'notaMediaVideojuego': nota,
        'criticas':criticas,
        'sitios':sitiosVideojuegoLeido,
        #'trailers':trailersVideojuegoLeido,
        'respuestas':respuestasCriticas,
        'puntuaciones':puntuacionesCriticas,
        'criticasValoradas':criticasValoradas,
        'qr':"img/qr.png",
    }
    context['logueado'] = 1
    return render(request, "gamerucos/videojuego.html", context)

def trailers(request, idVideojuego):
    if 'idUsuario' not in request.session:
        context = {
            'logueado':0,
            'mensaje':"No está permitido visualizar el trailer de un videojuego sin estar registrado",
        }
        return render(request, "gamerucos/error.html", context)
    videojuegoLeido = Videojuego.objects.get(id=idVideojuego)
    trailersVideojuegoLeido = Trailer.objects.filter(videojuego=videojuegoLeido).all()
    context = {
        'trailers':trailersVideojuegoLeido,
    }
    context['logueado'] = 1
    return render(request,"gamerucos/trailers.html",context)

def recomendaciones(request):
    if 'idUsuario' in request.session:
        context = {
            'logueado':1,
        }
    else:
        context = {
            'logueado':0,
        }
    return render(request, "gamerucos/recomendaciones.html", context)

def perfil(request, idUsuario):
    usuario = User.objects.get(id=idUsuario)
    criticas = Critica.objects.all().filter(autor=usuario)
    context = {
        'usuario':usuario,
        'criticas':criticas,
    }
    if 'idUsuario' in request.session:
        context['logueado'] = 1
    else:
        context['logueado'] = 0
    return render(request, "gamerucos/perfil.html", context)

def miPerfil(request):
    usuario = User.objects.get(id=request.session['idUsuario'])
    criticas = Critica.objects.all().filter(autor=usuario)
    context = {
        'usuario':usuario,
        'criticas':criticas,
    }
    if 'idUsuario' in request.session:
        context['logueado'] = 1
    else:
        context['logueado'] = 0
    return render(request, "gamerucos/perfil.html", context)

def logout(request):
    del request.session['idUsuario']    
    # logout(request)
    return redirect('home')

def valorarPositivo(request, idVideojuego, idCritica):
    critica=Critica.objects.get(id=idCritica)
    autor=User.objects.get(id=request.session['idUsuario'])
    valor=True
    valoracion=Valoracion.objects.create(critica=critica, autor=autor, valor=valor)
    valoracion.save()
    return redirect('videojuego', idVideojuego=idVideojuego)
    # return redirect('videojuego', critica.videojuego.id)

def valorarNegativo(request, idVideojuego, idCritica):
    critica=Critica.objects.get(id=idCritica)
    autor=User.objects.get(id=request.session['idUsuario'])
    valor=False
    valoracion=Valoracion.objects.create(critica=critica, autor=autor, valor=valor)
    valoracion.save()
    return redirect('videojuego', idVideojuego=idVideojuego)