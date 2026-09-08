from django.shortcuts import render

from django.views.generic import DetailView, ListView, TemplateView

from django.views import View

from catalog.models import Product


class HomeView(ListView):
    """Отображает главную страницу."""
    model = Product
    template_name = "home.html"
    context_object_name = "products"

class ContactsView(View):
    """Отображает страницу контактов."""

    def get(self, request):
        return render(request, "contacts.html")

    def post(self, request):
        return render(request, "contacts.html", {"success": True})

class ProductView(DetailView):
    """Отображает товар."""

    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"
