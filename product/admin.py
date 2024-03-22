from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline,]
    list_display = ('name', 'owner', 'category', 'rating', 'deleted')
    list_filter = ('category', 'deleted', 'rating')
    search_fields = ('name', 'description')

admin.site.register(Product, ProductAdmin)
