from django.shortcuts import render

def sobre(request):
    return render(request, 'rdr2_app/sobre.html')

def perfil(request):
    return render(request, 'rdr2_app/perfil.html')

def contato(request):
    return render(request, 'rdr2_app/contato.html')
