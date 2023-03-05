from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.text import slugify

from product.models import Product, Category
from .forms import SignUpForm, ProductForm

# Create your views here.
def frontpage(request):
    products = Product.objects.filter(status=Product.ACTIVE)[0:8]

    return render(request, 'core/frontpage.html', {'products': products})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/')

    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            name = request.POST.get('name')
            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(name)
            product.save()

            messages.success(request, 'Product Added.')

        return redirect('shop')
    else:
        form = ProductForm()

    return render(request, 'core/add_product.html',{
        'title': 'Add Product',
        'form': form
    })

@login_required
def edit_product(request, pk):
    product = Product.objects.get(pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()

            messages.success(request, 'Changes Saved.')

            return redirect('shop')

    else:
        form = ProductForm(instance=product)
    
    return render(request, 'core/add_product.html',{
        'title': 'Edit Product',
        'product': product, 
        'form': form
    })

@login_required
def delete_product(request, pk):
    product = Product.objects.get(pk=pk)
    product.status = Product.DELETED
    product.save()
    
    messages.success(request, 'Product Deleted.')

    return redirect('shop')

@login_required
def myaccount(request):
    return render(request, 'core/myaccount.html')

@login_required
def edit_myaccount(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()

        return redirect('myaccount')

    return render(request, 'core/edit_myaccount.html')

def shop(request):
    categories = Category.objects.all()
    products = Product.objects.exclude(status=Product.DELETED)

    active_category = request.GET.get('category','')

    if active_category:
        products = products.filter(category__slug=active_category)

    query = request.GET.get('query', '')

    if query:
        products = products.filter(status=Product.ACTIVE).filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(author__icontains=query) | Q(isbn13__icontains=query))


    context = {
        'categories': categories,
        'products': products,
        'active_category': active_category
    }

    return render(request, 'core/shop.html', context)
