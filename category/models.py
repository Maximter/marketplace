from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    cover = models.ImageField(upload_to='category_covers/', verbose_name='Cover')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
