from django.shortcuts import render, get_object_or_404
from .models import Article


def index(request):
    # most recent article
    latest_article = Article.objects.all().order_by('-pub_date').first()

    # most recent articles
    latest_articles = Article.objects.all().order_by('-pub_date')[:8]

    data = {
        'latest_article': latest_article,
        'latest_articles': latest_articles
    }
    return render(request, 'index.html', data)


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def articles(request):
    articles = Article.objects.all().order_by('-pub_date')
    data = {
        'articles': articles
    }
    return render(request, 'articles.html', data)


def articles_detail(request, id=None):
    article = get_object_or_404(Article, pk=id)
    related_articles = Article.objects.filter(category=article.category)[:4]
    data = {
        'article': article,
        'related_articles': related_articles
    }
    print(article)
    return render(request, 'articles-detail.html', data)
