from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def contacto(request):
    contacto = "Edwin Salgado"
    list_directions = ['Av Olmos num 13 Ciudad de Mèxico',
    'Calle Benito Juearez num 123, Estado de México']

    administradores = [
        {'nombre':"Luis",'apellidos':"Salazar Torres",'email':"ltorres@gmail.com",'encargado':True},
        {'nombre':"María",'apellidos':"Ruíz Gutierrez",'email':"mrg@gmail.com",'encargado':False},
        {'nombre':"Diego",'apellidos':"Barriga Martínez",'email':"dbm@gmail.com",'encargado':False}
    ]
    return render(request,'contacto.html',{'contacto1':contacto,
    'direcciones':list_directions,'admins':administradores})
