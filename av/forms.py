from django import forms
from django.forms import ModelForm, TextInput

from .models import Product

class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ['model', 'marka', 'price', 'year', 'url']
        widgets = {
            'model': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Модель автомобиля'
            }),
            'marka': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Марка автомобиля'
            }),
            'price': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена автомобиля'
            }),
            'year': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Год изготовления автомобиля'
            }),
            'url': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'URL адрес объявления'
            }),
        }