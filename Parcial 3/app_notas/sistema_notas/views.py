from django.shortcuts import redirect,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator
from datetime import datetime

from .forms import NotasForm
from .models import Nota


def VerNota(request):
          
    obj = get_object_or_404(Nota, id = id)
    #Consultar datos de producto
    
    #Obtener el template
    template = loader.get_template("VerNota.html")

    return HttpResponse(template.render(context,request))

# Vista principal de Gestión de Productos
def GestionNota(request):
    #Consultar productos
    notas_list = Nota.objects.all()
    #Configurar paginación cada 10 productos
    paginator = Paginator(notas_list, 10)

    #Obtener página
    page_number = request.GET.get('page',0)
    page_obj = paginator.get_page(page_number)

    #Obtener el template
    template = loader.get_template("GestionNota.html")
    #Agregar el contexto
    context = {"page_obj": page_obj}
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

# Vista para crear productos
def CrearNota(request):
    #Obtener el template
    template = loader.get_template("CrearNota.html")
    #Generar Formulario
    if request.method == "POST":
        form = NotasForm(request.POST or None, request.FILES)
        if form.is_valid():
            #obtener datos del formulario
            nota_nuevo = form.save(commit=False)
            #Asignar fecha de creación
            nota_nuevo.fecha_creacion = datetime.now()
            #Guardar Producto
            nota_nuevo.save()
            return redirect('gestionNota')
    else:
        form = NotasForm()
    #Crear contexto
    context = {}
    context['form'] = form
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

# Vista de Productos
def EditarNota(request,id):
    #Obtener el template
    template = loader.get_template("EditarNota.html")
    #Buscar Producto
    obj = get_object_or_404(Nota, id = id)
    #formulario que contiene la instancia
    form = NotasForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('gestionNota')   
    #Agregar el contexto
    context = {}
    context['form'] = form
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))

# Vista de Productos
def BorrarNota(request,id):
    #Obtener el template
    template = loader.get_template("BorrarNota.html")
    #Buscar el producto
    obj = get_object_or_404(Nota, id = id)
    if request.method == "POST":
        obj.delete()
        return redirect('gestionNota')
    #Agregar el contexto
    context = {}
    #Retornar respuesta http
    return HttpResponse(template.render(context,request))