from django.shortcuts import render, redirect
from .models import Product
from django.core import management
from django.http import HttpResponse
from .forms import ProductForm

import pandas as pd
import plotly.express as px
import plotly as plotly

def index(request):
    items = Product.objects.all()

    dct = {}

    for i in items:
        dct[i.marka] = dct.get(i.marka, 0) + 1
    
    counts = [int(i) for i in dct.values()]
    marks = [i for i in dct]
    total = sum(counts)
    df = pd.DataFrame({'marks': marks, 'counts': counts})
    
    fig = px.bar(df, y='counts', x='marks', text_auto='.2s')
    #fig.show()

    plotly.offline.plot(fig, filename='av/static/img/doc.html')

    plotly.io.write_image(fig, file='av/static/img/my_figure_file.png', format='png', scale=None, width=None, height=None)

    return render(request, 'av/index.html', {'marks': marks, 'counts': counts, 'dct': dct, 'total': total})


def refresh(request):
    management.call_command('av_parse')
    return render(request, 'av/index.html')

def clear(request):
    management.call_command('migrate av zero')
    management.call_command('migrate')

def news(request):
    return render(request, 'av/news_home.html')

def cars(request):
    #items = Product.objects.all()
    #items = Product.objects.order_by('price')
    items = Product.objects.order_by('marka')
    dct = {}
    dct1 = {}

    for i in items:
        dct[i.marka] = dct.get(i.marka, 0) + 1
    
    for j in items:
        dct1[j.marka] = dct1.get(j.marka, []) + [j.model, j.year, j.price, j.url]

    counts = [int(i) for i in dct.values()]
    marks = [i for i in dct]
    total = sum(counts)

    return render(request, 'av/cars.html', {'total': total, 'items': items})

def contacts(request):
    return render(request, 'av/contacts.html')
