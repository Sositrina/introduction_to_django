from django.shortcuts import render

from catalog.models import Product

def home(request):
    """Отображает главную страницу."""
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def contacts(request):
    """Отображает страницу контактов."""
    if request.method == 'POST':
        return render(request, 'contacts.html', {'success': True})

    return render(request, 'contacts.html')

def product_detail(request, pk):
    """Отображает товар."""

    product = Product.objects.get(pk=pk)

    return render(
        request,
        "product_detail.html",
        {"product": product},
    )
