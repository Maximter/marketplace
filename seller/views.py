from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.contenttypes.models import ContentType
from authentication.decorators import group_required
from authentication.models import CustomUser
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group

# Create your views here.
@group_required('Sellers')
def index(request):
    context = {'name': request.user.first_name}
    return render(request, 'seller.html', context)

@login_required
def create(request):
    if request.user.groups.filter(name='Sellers').exists():
        return redirect('seller')

    if request.method == 'POST':
        user = request.user
        try:
            sellers_group = Group.objects.get(name='Sellers')
            user.groups.add(sellers_group)
        except Permission.DoesNotExist:
            print("Permission doesn't exist")
        return redirect('seller')  

    context = {'name': request.user.first_name}
    return render(request, 'create.html', context)
