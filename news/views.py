import os

from django.urls import reverse

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

from news.forms import NewComment
from news.models import NewsArticle, Comment
from news.forms import NewsArticleForm
from quant_site import settings


def news_list(request):

    news = NewsArticle.objects.all()
    return render(request, 'news/news_list.html', context={'news': news})

def news_detail(request, news_id):
    new = NewsArticle.objects.get(pk=news_id)
    comments = new.comments.all()
    if request.method == 'POST':
        form = NewComment(request.POST)
        if form.is_valid():
            Comment.objects.create(
                article = new,
                text=form.cleaned_data["text"],
                )
            url = reverse('news:detail', kwargs={'news_id': news_id})
            return redirect(url)
    else:
        form = NewComment()


    return render(request, 'news/news_detail.html', context={
        'new': new,
        'comments': comments,
        'form': form,
    })

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
