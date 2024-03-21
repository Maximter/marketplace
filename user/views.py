from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    context = {'name': request.user.first_name, 'seller': request.user.groups.filter(name='Sellers').exists()}
    return render(request,  'user.html', context)