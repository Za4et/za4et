from django.shortcuts import render, get_object_or_404

# Create your views here.
from news.models import News


def news(request):
    news = {'news': News.objects.all()}
    return render(request, 'news.html', news)


def article(request, year, month, day, slug):
    article = get_object_or_404(News, published__year=year, published__month=month, published__day=day, slug=slug)
    return render(request, 'article.html', {'article': article})
