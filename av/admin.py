from django.contrib import admin

from .models import *
from .forms import ProductForm


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('model', 'marka', 'price', 'year', 'url')
    list_filter = ('marka', )
    form = ProductForm

