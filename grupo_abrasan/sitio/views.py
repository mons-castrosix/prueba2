from django.shortcuts import render

# Create your views here.
def panel(request):
   
    
    return render(request,'sitio/index.html')

def nosotros(request):
    return render(request,'sitio/nosotros.html')


def mision(request):
    return render(request,'sitio/mision.html')
def vision(request):
    return render(request,'sitio/vision.html')