from django.shortcuts import render

# Create your views here.


def login(request):
    context = {
        'name': 'login'
    }

    return render(request, 'login/login.html', context)
