from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroForm

# 🧩 Vista de registro
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['password1'])  # Cifra correctamente la contraseña
            usuario.save()
            login(request, usuario)
            return redirect('usuarios:login')  # 🔄 Redirige al perfil al crear cuenta
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})


# 👤 Vista de perfil (solo mostrar)
@login_required
def perfil_usuario(request):
    usuario = request.user
    return render(request, 'usuarios/perfil.html', {'usuario': usuario})


# ✏️ Vista para editar perfil (desde el modal)
@login_required
def editar_perfil(request):
    usuario = request.user

    if request.method == 'POST':
        usuario.first_name = request.POST.get('nombre')
        usuario.last_name = request.POST.get('apellido')
        usuario.telefono = request.POST.get('telefono')
        usuario.direccion = request.POST.get('direccion')
        usuario.save()

        messages.success(request, "Tu perfil se ha actualizado correctamente ✅")
        return redirect('usuarios:perfil_usuario')

    return redirect('usuarios:perfil_usuario')
