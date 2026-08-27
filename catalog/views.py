from django.shortcuts import render

def home(request):
    """Отображает главную страницу."""
    return render(request, 'home.html')

def contacts(request):
    """Отображает страницу контактов."""
    if request.method == 'POST':
        return render(request, 'contacts.html', {'success': True})

    return render(request, 'contacts.html')
