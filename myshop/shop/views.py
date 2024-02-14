from django.shortcuts import render, get_object_or_404, redirect
from cart.forms import CartAddProductForm
from .models import Category, Product
from .forms import ProductEditForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    remaining_quantity = product.total_quantity - product.sold_quantity
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'remaining_quantity': remaining_quantity})


def product_edit(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    if request.method == 'POST':
        form = ProductEditForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            if not product.available:
                # Redirect to the main product list page if not available
                return redirect('shop:product_list')
            # Redirect to the updated product detail page
            return redirect('shop:product_detail', id=product.id, slug=product.slug)
    else:
        form = ProductEditForm(instance=product)
    return render(request,
                  'shop/product/edit.html',
                  {'product': product,
                   'form': form})