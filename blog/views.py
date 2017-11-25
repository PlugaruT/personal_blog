from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    # ultimul articol
    latest_article = Article.objects.all().order_by('-pub_date').first()

    # cele mai recente 4 articole
    last_4_articles = Article.objects.all().order_by('-pub_date')[:4]

    data = {
        'latest_article': latest_article,
        'last_4_articles': last_4_articles
    }
    return render(request, 'index.html', data)


def about(request):
    return render(request, 'about.html')