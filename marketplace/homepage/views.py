from django.shortcuts import render

# Create your views here.

def index(request):
    context = {'message': 'Привет, мир!'}
    return render(request,  '../homepage/templates/homepage/index.html', context)