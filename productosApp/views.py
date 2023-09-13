from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'productosApp/index.html')

def consolas(request):
    data= {
        'titulo': 'Consolas'
    }
    return render(request,'productosApp/template.html',data)

def electro(request):
    data= {
        'titulo': 'Electronica'
    }
    return render(request,'productosApp/template.html',data)

def ropa(request):
    data= {
        'titulo': 'Ropa'
    }
    return render(request,'productosApp/template.html',data)