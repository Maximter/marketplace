from django.shortcuts import render

from authentication.decorators import group_required
from django.shortcuts import render, redirect

from product.models import Product, ProductImage
from .forms import ProductForm, ProductImageForm
from django.forms import modelformset_factory


def index(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return redirect('home')
    images = ProductImage.objects.filter(product=product)
    context = {'product': product, 'images': images}
    return render(request, 'product.html', context)



@group_required('Sellers')
def create(request):
    # Создаём формсет для изображений, позволяя добавить 3 дополнительных формы
    ImageFormSet = modelformset_factory(ProductImage, form=ProductImageForm, extra=3, max_num=10)
    
    if request.method == 'POST':
        productForm = ProductForm(request.POST)
        # Обратите внимание: 'files' передаём в formset для обработки загруженных файлов
        formset = ImageFormSet(request.POST, request.FILES, queryset=ProductImage.objects.none())
        print(productForm.is_valid(), formset.is_valid())
        if productForm.is_valid() and formset.is_valid():
            product = productForm.save(commit=False)
            product.owner = request.user  # Установка владельца продукта, если требуется
            product.save()

            for form in formset:
                # Проверяем, есть ли данные в каждой форме изображения
                if form.cleaned_data:
                    image = form.cleaned_data.get('image')
                    if image:
                        ProductImage.objects.create(product=product, image=image)
            # Перенаправление после успешного создания продукта и его изображений
            return redirect(f'/product/{product.id}')
        else:
            # Выводим ошибки в консоль для диагностики
            print("Product form errors:", productForm.errors)
            print("Formset errors:", formset.errors)
    else:
        productForm = ProductForm()
        formset = ImageFormSet(queryset=ProductImage.objects.none())

    return render(request, 'create_product.html', {
        'productForm': productForm,
        'formset': formset
    })
