from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if request.user.is_authenticated:
        context = {'name': request.user.first_name}
    else:
        context = {'name': None}
    return render(request,  'user.html', context)