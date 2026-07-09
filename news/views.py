from django.shortcuts import render, redirect
from django.urls import reverse

from news.forms import NewComment
from news.models import NewsArticle, Comment


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
    return render(request, 'news/news_add.html', context={})

# Create your views here.
