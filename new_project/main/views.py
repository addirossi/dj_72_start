from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from main.models import Product


def index(request):
    return HttpResponse('HELLO WORLD!')


def products_list(request):
    products = Product.objects.all()
    # добавляем отображение
    # return HttpResponse(products)
    return render(request, 'main/list.html', {'products': products})


def product_details(request, prod_id):
    print(f'ID товара: {prod_id}')
    print('CHHEEEECKK!!!')
    try:
        product = Product.objects.get(id=prod_id)
        return render(request, 'main/details.html', {'product': product})
    except Product.DoesNotExist:
        raise Http404('Product not found')




