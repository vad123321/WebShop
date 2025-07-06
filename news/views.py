from django.shortcuts import render
from .models import News, NewsCategory


def index(request):

    all_news = News.objects.all()
    all_categories = NewsCategory.objects.all()

    return render(request, 'news/index.html', context={
        'title': 'Новини',
        'page': 'index',
        'app': 'news',
        'news': all_news,
        'categories': all_categories
    })


