from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    context = {'name': request.user.first_name}
    return render(request,  'user.html', context)