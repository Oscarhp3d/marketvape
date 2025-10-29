from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import RegistroForm

def register_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Tu cuenta fue creada con éxito 🎉')
            return redirect('productos:home')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})
