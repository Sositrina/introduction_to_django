from django.shortcuts import render

from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from django.views import View

from catalog.models import Product

from catalog.forms import ProductForm

from django.urls import reverse_lazy


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

class ProductCreateView(CreateView):
    """Создает новый продукт."""

    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("home")

class ProductUpdateView(UpdateView):
    """Редактирует продукт."""

    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("home")

class ProductDeleteView(DeleteView):
    """Удаляет продукт."""

    model = Product
    template_name = "product_confirm_delete.html"
    success_url = reverse_lazy("home")
