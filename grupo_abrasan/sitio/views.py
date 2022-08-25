from django.shortcuts import render

# Create your views here.
def panel(request):
    return render(request,'sitio/index.html')

def nosotros(request):
    return render(request,'sitio/vision.html')

def calidad(request):
    return render(request,'sitio/servicios-calidad.html')
def clientes(request):
    return render(request,'sitio/servicios-clientes.html')

def contacto(request):
    return render(request,'sitio/contacto.html')
def obras(request):
    return render(request,'sitio/obras.html')

