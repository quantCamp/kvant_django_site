from django.shortcuts import render

news = [
    {
        'name': 'КВН',
        'description': 'Сегодня в квн сыграли команды "ФМ-8", "Алты жиде", "Вожатые"'
    },
    {
        'name': 'ЧГК',
        'description': 'Сегодня в игре что где когда, шаян тв всех вынес'

    }
]

def index(request):
    """Отображает главную страницу летней физико-математической школы «Квант»."""
    return render(request, 'main/index.html')

def news_page(request):
    return render(request, 'news/news_list.html', context={'news': news})
