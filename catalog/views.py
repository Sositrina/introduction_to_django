from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponseForbidden

from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from django.views import View

from catalog.models import Product

from catalog.forms import ProductForm

from django.urls import reverse_lazy

from django.views.decorators.cache import cache_page

from django.utils.decorators import method_decorator

from catalog.services import get_products_by_category


class HomeView(ListView):
    """Отображает главную страницу."""
    model = Product
    template_name = "home.html"
    context_object_name = "products"


class ProductByCategoryView(ListView):
    """Отображает продукты указанной категории."""

    template_name = "products_by_category.html"
    context_object_name = "products"

    def get_queryset(self):
        """Возвращает продукты выбранной категории."""
        category_id = self.kwargs["category_id"]
        return get_products_by_category(category_id)


class ContactsView(View):
    """Отображает страницу контактов."""

    def get(self, request):
        return render(request, "contacts.html")

    def post(self, request):
        return render(request, "contacts.html", {"success": True})

@method_decorator(cache_page(60 * 15), name="dispatch")
class ProductView(LoginRequiredMixin, DetailView):
    """Отображает товар."""

    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"

class ProductCreateView(LoginRequiredMixin, CreateView):
    """Создает новый продукт."""

    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        """Назначает владельцем продукта текущего пользователя."""
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Редактирует продукт."""

    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        """Проверяет доступ к редактированию продукта."""
        product = self.get_object()

        if product.owner != request.user and not request.user.has_perm("catalog.can_unpublish_product"):
            return HttpResponseForbidden("У вас нет прав для редактирования продукта.")

        return super().dispatch(request, *args, **kwargs)

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Удаляет продукт."""

    model = Product
    template_name = "product_confirm_delete.html"
    success_url = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        """Проверяет доступ к удалению продукта."""
        product = self.get_object()

        if product.owner != request.user and not request.user.has_perm("catalog.delete_product"):
            return HttpResponseForbidden("У вас нет прав для удаления продукта.")

        return super().dispatch(request, *args, **kwargs)


class ProductUnpublishView(LoginRequiredMixin, View):
    """Отменяет публикацию продукта."""

    def post(self, request, pk):
        """Снимает продукт с публикации."""
        product = get_object_or_404(Product, pk=pk)

        if not request.user.has_perm("catalog.can_unpublish_product"):
            return HttpResponseForbidden("У вас нет прав для отмены публикации продукта.")

        product.is_published = False
        product.save()

        return redirect("home")
