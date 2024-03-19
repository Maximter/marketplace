from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.contenttypes.models import ContentType
from authentication.models import CustomUser
from django.contrib.auth.models import Permission

# Create your views here.
@permission_required("is_seller", raise_exception=False)
def index(request):
    context = {'name': request.user.first_name}
    return render(request, 'seller.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        user = request.user
        content_type = ContentType.objects.get_for_model(CustomUser)
        try:
            permission = Permission.objects.get(
                codename="is_seller",
                content_type=content_type,
            )
            user.user_permissions.add(permission)
            user.save()
        except Permission.DoesNotExist:
            print("Permission doesn't exist")
            raise(Exception)
        return redirect('seller')  

    context = {'name': request.user.first_name}
    return render(request, 'create.html', context)
