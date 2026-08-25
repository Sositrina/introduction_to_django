from django.urls import path
from catalog.views import home, contacts


# Маршруты приложения
urlpatterns = [
    path('', home),
    path('contacts/', contacts),
]