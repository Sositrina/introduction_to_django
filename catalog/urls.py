from django.urls import path
from catalog.views import (
    HomeView,
    ContactsView,
    ProductView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductUnpublishView)

# Маршруты приложения
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('contacts/', ContactsView.as_view()),
    path("products/<int:pk>/", ProductView.as_view(), name="product_detail"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("products/<int:pk>/unpublish/", ProductUnpublishView.as_view(), name="product_unpublish"),
]
