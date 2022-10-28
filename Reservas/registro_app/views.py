from cgitb import reset
from django.shortcuts import render, redirect
from registro_app.models import reserva
from registro_app.forms import FormRegistro

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listadoreservas(request):
    reservas = reserva.objects.all()
    data = {'reservas': reservas}
    return render(request, 'registroreserva.html', data)

def agregarreserva(request):
    form = FormRegistro()
    if request.method == 'POST':
        form = FormRegistro(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarreserva.html', data)

def eliminarReserva(request, id):
    pro = reserva.objects.get(id = id)
    pro.delete()
    return redirect('/registroreserva')

def actualizarReserva(request, id):
    pro = reserva.objects.get(id = id)
    form = FormRegistro(instance=pro)
    if request.method == 'POST':
        form = FormRegistro(request.POST, instance=pro)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarreserva.html', data)
