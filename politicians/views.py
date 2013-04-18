# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from politicians.models import Politician, News, User
from datetime import datetime, timedelta

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

def news_search(request):
    return render(request, 'politicians/news_search.html')

def news_search_results(request):
    try:
        keywords = request.POST['keywords']
        date_option = request.POST['time']
    except:
        return render(request, 'politicians/news_search_results.html')

    if date_option == 'this_week':
        minimum_date = datetime.now() - timedelta(days=7)
    elif date_option == 'this_month':
        minimum_date = datetime.now() - timedelta(days=30)
    elif date_option == 'this_year':
        minimum_date = datetime.now() - timedelta(days=365)
    else:
        minimum_date = None
    
    word_list = keywords.split()
    
    results = []
    for word in word_list:
        if minimum_date is None:
            ans = News.objects.filter(title__contains=word)
        else:
            ans = News.objects.filter(title__contains=word,pub_date__gte=minimum_date)
        results = list(set(results) | set(ans))
    context = {'results' : results }
    return render(request, 'politicians/news_search_results.html', context)

def news(request):
    news_list = News.objects.all().order_by('-pub_date')[:5]          

    try:
        username = request.session['username']
        user = User.objects.get(username__exact=username)
        user_logged_in = True
    except KeyError, User.DoesNotExist:
        user_logged_in = False

    news_liked_id = request.POST.get('liked',None)
    try:
        news_liked = News.objects.get(id=news_liked_id)
        user.like_news(news_liked)
    except:
        pass

    news_unliked_id = request.POST.get('unliked',None)
    try:
        news_unliked = News.objects.get(id=news_unliked_id)
        user.unlike_news(news_unliked)
    except:
        pass


    news_like_count = []
    for news in news_list:
        news_like_count.append(news.get_likes_count())

    news_like_status = []
    for news in news_list:
        if user_logged_in:
            news_like_status.append(news.does_user_like_me(user))
        else:
            news_like_status.append(None)

    news_entry = zip(news_list,news_like_count,news_like_status)
    
    context = {'news_heading': 'Notícias Recentes', 'news_entry': news_entry}
    return render(request, 'politicians/news.html', context)

def all_news(request):
    news_list = News.objects.all().order_by('-pub_date')
    context = {'news_heading': 'Notícias', 'news_list': news_list}
    return render(request, 'politicians/news.html', context)

def login(request):
	return render(request, 'politicians/login.html')
	
def login_user(request):
        #FIXME: This raises an exception if you type /login_user directly
        #in the browser
	name = request.POST['name']
	try:
		user = User.objects.get(username=request.POST['name'])
	except User.DoesNotExist:
		context = {'message': "Usuario inexistente"}
		return render(request, 'politicians/login.html', context)
	if user.password == request.POST['password']:
		request.session['username'] = user.username
		context = {'message': "logado"}
		return render(request, 'politicians/home.html', context)
	else:
		context = {'message': "Senha incorreta"}
		return render(request, 'politicians/login.html', context)
	
def logout(request):
	del request.session['username']
	return render(request, 'politicians/home.html')
	
def search(request):
    return render(request, 'politicians/search.html')

def search_results(request):
    name = request.POST['name']
    politicians_list = Politician.objects.filter(name__contains=name)
    context = {'politicians_list': politicians_list}
    return render(request, 'politicians/politicians.html', context)

def home(request):
    return render(request, 'politicians/home.html')
