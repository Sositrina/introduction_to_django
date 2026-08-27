from django.urls import path
from catalog.views import home, contacts, product_detail

# Маршруты приложения
urlpatterns = [
    path('', home),
    path('contacts/', contacts),
    path("products/<int:pk>/", product_detail, name="product_detail"),
]
