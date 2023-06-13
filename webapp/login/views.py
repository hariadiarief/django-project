from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import FormLogin

from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.


def login_view(request):
    form = FormLogin()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/login/dashboard')

    return render(request, 'login/login.html', {'form': form})


@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    context = {}
    return render(request, 'login/dashboard.html', context)


def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('/login/')
