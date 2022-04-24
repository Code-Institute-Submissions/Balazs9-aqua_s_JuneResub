from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Category
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """ A view to show all products """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def mineral_water(request):
    """ A view to show only the mineral waters """

    product = Product.objects.filter(category__name='mineral_water')

    return render(request, 'products/products.html', {
        'product': product,
    })


def sport_drink(request):
    """ A view to show only the sport drinks """

    product = Product.objects.filter(category__name='sport_drink')

    return render(request, 'products/products.html', {
        'product': product,
    })


def water_dispenser(request):
    """ A view to show only the water dispenser machines """

    product = Product.objects.filter(category__name='water_dispenser')

    return render(request, 'products/products.html', {
        'product': product,
    })


def product_detail(request, product_id):
    """ A view to show informations about the product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """
    Add product to the store
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
