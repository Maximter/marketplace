from django.shortcuts import render

from authentication.decorators import group_required

# Create your views here.

def index(request):
    context = {'name': request.user.first_name}
    return render(request, 'product.html', context)

@group_required('Sellers')
def create(request):
    if request.method == 'POST':
        user = request.user
        # try:
        #     sellers_group = Group.objects.get(name='Sellers')
        #     user.groups.add(sellers_group)
        # except Permission.DoesNotExist:
        #     print("Permission doesn't exist")
        # return redirect('seller')  

    context = {'name': request.user.first_name}
    return render(request, 'create_product.html', context)
