from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import OuterRef, Subquery
from category.models import Category
from product.models import ProductImage

# Create your views here.
def index(request):
    categories = Category.objects.all()
    return render(request, 'all_categories.html', {'categories': categories })

def category(request, category_name):
    category = get_object_or_404(Category, name=category_name)

    products_with_first_image = category.products.annotate(
        first_image=Subquery(
            ProductImage.objects.filter(
                product=OuterRef('pk')
            ).order_by('id').values('image')[:1]
        )
    )
    return render(request, 'category.html', {'category': category, 'products': products_with_first_image})