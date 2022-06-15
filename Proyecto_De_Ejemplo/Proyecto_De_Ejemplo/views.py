from contextvars import Context
from django.http import HttpResponse
from django.template import Template, context
import datetime
from datetime import date
def saludo(request):
    return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :) ")

def dia_de_hoy(request):
    dia = datetime.datetime.now()
    documento_de_texto = f"Hoy es dia: <br> {dia}"

    return HttpResponse(documento_de_texto)

def MiNombreEs(self, nombre):
    DocumentoDeTexto = f"mi nombre es: <br><br> {nombre}"

    return HttpResponse(DocumentoDeTexto)

def TerceraVista(request, fecha):
    FechaActual = date.today()
    Anio = FechaActual.year
    Fecha = int(fecha)
    Resultado = Anio - Fecha
    Retorno = f'el año en que naciste es: {Resultado} '
    return HttpResponse(Retorno)

def probandoTemplate(self):
    miHtml = open("C:/Users/Equipo/Desktop/Django3/Proyecto_De_Prueba/Proyecto_De_Ejemplo/Proyecto_De_Ejemplo/plantillas/template1.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)