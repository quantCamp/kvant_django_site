import os

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from news.forms import NewsArticleForm
from news.models import NewsArticle
from quant_site import settings


def news_list(request):
    news_listik= NewsArticle.objects.all()
    return render(request, 'news/news_list.html', context={'news_listik': news_listik})

def news_detail(request):
    return render(request, 'news/news_detail.html')

def news_add(request):
    if request.method == 'POST':
        form = NewsArticleForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['img']
            filename = upload_news_image(file)
            NewsArticle.objects.create(title=form.cleaned_data['title'], text=form.cleaned_data['text'], img=filename)
    else:
        form = NewsArticleForm()
    return render(request, 'news/news_add.html', context={'form': form})


def upload_news_image(file):
    fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'img'))
    filename = fs.save(file.name, file)
    relative_path = os.path.join('img', filename)
    return relative_path

# Create your views here.
