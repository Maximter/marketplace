from django.shortcuts import render

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        context = {'name': request.user.first_name}
    else:
        context = {'name': None}
    return render(request,  'homepage.html', context)