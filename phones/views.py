from django.shortcuts import render, redirect

import phones
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.object.all()
    context = {
        'phones': phones
    }
    return render(request, template, context)


# def show_product(request, slug):
#     template = 'product.html'
#     context = {
#         'phone': phone
#     }
#     return render(request, template, context)
