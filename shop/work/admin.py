from django.contrib import admin
from .models import Category, Product



# Модель категории
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

# Модель товара
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price',]
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name', )}
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
