from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render


def miRuta(request):
    return HttpResponse("Hola desde mi ruta")


def miotraRuta(request):
    return HttpResponse("esta es mi otra ruta xd")


def saludo(request):
    # creando el doc ext
    marcas = ["sony", "samsung", "huawei"]
    nombre = "juan"
    apellido = "perez"
    ahora = datetime.datetime.now()

    # doc_exter = open(
    # "/home/larz/Escritorio/Projectos/python_django/frst/frst/plantillas/plantilla.html")

    # plt = Template(doc_exter.read())

    doc_externo = loader.get_template('plantilla.html')
    # doc_exter.close()

    # ctx = Context({"nombre_persona": nombre,
#              "apellido_persona": apellido, "ahora": ahora, "Marcas": marcas})

    # documento = doc_externo.render({"nombre_persona": nombre,
    #                               "apellido_persona": apellido, "ahora": ahora, "Marcas": marcas})
    datos = {"nombre_persona": nombre, "apellido_persona": apellido,
             "ahora": ahora, "Marcas": marcas}

    return render(request, "plantilla.html", datos)


def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """
        <h2>fecha actual %s </h2>
    """ % fecha_actual
    return HttpResponse(documento)


def calculaEdad(request, edad, year):

    periodo = year-2019
    edadFutura = edad+periodo

    document = """<h2>en el %s tendras %s """ % (year, edadFutura)
    return HttpResponse(document)
