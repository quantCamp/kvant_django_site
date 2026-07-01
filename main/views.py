from django.shortcuts import render

def index(request):
    """Отображает главную страницу летней физико-математической школы «Квант»."""
    return render(request, 'main/index.html')
