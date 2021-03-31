from django.shortcuts import render

from news.models import Article

from utils.debug_utils import *

def get_homepage(request):
    return render(request, "base.html")

def year_archive(request, year):
    """Render articles on a specified year."""
    articles = Article.objects.filter(pub_date__year=year)
    context = { 'year': year, 'articles': articles }
    return render(request, 'news/year_archive.html', context)

def month_archive(request, year, month):
    """Render articles on a specified month on a specific year."""
    articles = Article.objects.filter(pub_date__year=year, pub_date__month=month)
    context = { 'year': year, 'month': month, 'articles': articles }
    pprint_local_vars(locals())
    return render(request, 'news/month_archive.html', context)

def article_detail(request, pk):
    """Render article detail."""
    article = Article.objects.get(pk=pk)
    context = { 'pk':pk, 'article': article }
    return render(request, 'news/article_detail.html', context)