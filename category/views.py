from django.shortcuts import render, redirect

from category.models import Category

# Create your views here.
def index(request):
    categories = Category.objects.all()
    return render(request, 'all_categories.html', {'categories': categories })

def category(request, category_name):
    try:
        category = Category.objects.get(name=category_name)
    except Category.DoesNotExist:
        return redirect('home')
    
    return render(request, 'category.html', {'category': category})