from django.urls import path
from catalog.views import HomeView, ContactsView, ProductView

# Маршруты приложения
urlpatterns = [
    path('',HomeView.as_view()),
    path('contacts/', ContactsView.as_view()),
    path("products/<int:pk>/", ProductView.as_view(), name="product_detail"),
]
