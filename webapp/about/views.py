from django.shortcuts import render

# Create your views here.


def index( request): 
    context = {
        'name': 'hello world',
    }

    return render(request, 'index.html', context)
