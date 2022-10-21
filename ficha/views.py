from django.shortcuts import render
# from .models import IdentificacionInmueble, PlanoUbicacion, FotografiaGeneral, ResenaPatrimonial, ValoracionAtributos
from .models import *

# Create your views here.
def ficha_home(request):
    # identificacion_inmueble = IdentificacionInmueble.objects.all()
    # plano_ubicacion = PlanoUbicacion.objects.all()
    # fotografia_general = FotografiaGeneral.objects.all()
    # resena_patrimonial = ResenaPatrimonial.objects.all()
    # valoracion_atributos = ValoracionAtributos.objects.all()

    data = {}
    return render(request, 'ficha/home.html', data)

def crear_ficha(request):
    data = {}
    return render(request, 'ficha/crear_ficha.html', data)

def editar_ficha(request, id = 0):
    data = {}
    return render(request, 'ficha/editar_ficha.html', data)

def ver_fichas(request):
    identificacion_inmueble = IdentificacionInmueble.objects.all()

    data = {
        'fichas': identificacion_inmueble
    }
    return render(request, 'ficha/ver_fichas.html', data)

def ver_ficha(request, id):
    identificacion_inmueble = IdentificacionInmueble.objects.get(id_plano = id)
    plano_ubicacion = PlanoUbicacion.objects.get(id_plano = id)

    data = {
        'identificacion_inmueble': identificacion_inmueble,
        'plano_ubicacion': plano_ubicacion,
    }
    return render(request, 'ficha/ver_ficha.html', data)

def exportar_pdf(request, id):
    data = {}
    return render(request, 'ficha/exportar_pdf.html', data)