from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username = cd['nombre'],
                password = cd['contraseña'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('usuario autenticado')
                else:
                    return HttpResponse('el usuario no esta activo')
            else:
                return HttpResponse('usuario no valido')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})            