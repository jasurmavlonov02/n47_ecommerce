from django.shortcuts import render, redirect

from app.forms import ProductForm, ProductModelForm
from app.models import Product


# Create your views here.


def index(request):
    products = Product.objects.all().order_by('-id')[:4]
    context = {
        'products': products
    }
    return render(request, 'app/index.html', context)


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    attributes = product.get_attributes()

    context = {
        'product': product,
        'attributes': attributes
    }
    return render(request, 'app/product-detail.html', context)


# def add_product(request):
#     form = ProductForm()
#     # form = None
#     if request.method == 'POST':
#
#         name = request.POST['name']
#         description = request.POST['description']
#         price = request.POST['price']
#         rating = request.POST['rating']
#         discount = request.POST['discount']
#         quantity = request.POST['quantity']
#         form = ProductForm(request.POST)
#         product = Product(name=name, description=description, price=price, discount=discount, quantity=quantity,
#                           rating=rating)
#
#         if form.is_valid():
#             product.save()
#             return redirect('index')
#
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'app/add-product.html', context)


def add_product(request):
    form = ProductModelForm()
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'app/add-product.html', context)
