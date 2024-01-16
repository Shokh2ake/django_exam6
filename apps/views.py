# from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect

from apps.models import Product


def index(request):
    context = {
        'products': Product.objects.order_by('-price', 'id')
    }
    return render(request, 'apps/product/product_list.html', context)


def add_product(request):
    if request.method == 'POST':
        Product.objects.create(
            title=request.POST['title'],
            price=request.POST['price'],
            category_id=request.POST['category'],
            image=request.FILES['image'],
            quantity=request.POST['quantity']
        )
        return redirect('index')
    return render(request, 'apps/product/product_add.html')


def delete_product(request, pk):
    Product.objects.filter(id=pk).delete()
    return redirect('index')
