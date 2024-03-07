from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'name': 'Maxim'}
    return render(request,  'homepage/index.html', context)