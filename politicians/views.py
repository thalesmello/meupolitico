# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from politicians.models import Politician, News

def index(request):
    return render(request, 'politicians/index.html')

def politicians(request):
    politicians_list = Politician.objects.all().order_by('name')
    context = {'politicians_list': politicians_list}
    return render(request, 'politicians/politicians.html', context)

def politician_profile(request, politician_id):
    politician = get_object_or_404(Politician, pk=politician_id)
    recent_news = politician.news_set.all().order_by('-pub_date')[:5]
    context = {'politician': politician, 'recent_news': recent_news}
    return render(request, 'politicians/politician_profile.html', context)

def news(request):
    news_list = News.objects.all().order_by('-pub_date')[:5]
    context = {'news_heading': 'Notícias Recentes', 'news_list': news_list}
    return render(request, 'politicians/news.html', context)

def all_news(request):
    news_list = News.objects.all().order_by('-pub_date')
    context = {'news_heading': 'Notícias', 'news_list': news_list}
    return render(request, 'politicians/news.html', context)

def search(request):
    return render(request, 'politicians/search.html')

def search_results(request):
    name = request.POST['name']
    politicians_list = Politician.objects.filter(name__contains=name)
    context = {'politicians_list': politicians_list}
    return render(request, 'politicians/politicians.html', context)
