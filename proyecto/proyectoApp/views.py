from django.shortcuts import render

# Create your views here.
def formulario(request):
    print('el metodo es:',request.POST)
    data=request.POST
    print('datos',data['nombre'])
    print('datos cargo',data['cargo_proyecto'])
    return render(request,'formulario.html')