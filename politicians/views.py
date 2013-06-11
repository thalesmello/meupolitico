# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from politicians.models import Politician, News, User
from django.utils import timezone
from datetime import timedelta
from crawler import add_news_to_db

def home(request):
    return render(request, 'politicians/home.html')

def politicians(request):
    politicians_list = Politician.objects.all().order_by('name')
    context = {'politicians_list': politicians_list}
    return render(request, 'politicians/politicians.html', context)

def ranking(request):
    politicians_list = Politician.objects.all().order_by('-estrela5')
    context = {'politicians_list': politicians_list}
    return render(request, 'politicians/ranking.html', context)

def politician_profile(request, politician_id):
    politician = get_object_or_404(Politician, pk=politician_id)
    recent_news = politician.relevant_news.all().order_by('-pub_date')[:5]
    is_favorited = False
    try:
        username = request.session['username']
        user = User.objects.get(username__exact=username)
        is_favorited = user.has_favorited(politician)
    except KeyError, User.DoesNotExist:
        pass
    context = {'politician': politician, 'recent_news': recent_news, 'is_favorited': is_favorited}
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
        minimum_date = timezone.now() - timedelta(days=7)
    elif date_option == 'this_month':
        minimum_date = timezone.now() - timedelta(days=30)
    elif date_option == 'this_year':
        minimum_date = timezone.now() - timedelta(days=365)
    else:
        minimum_date = None

    word_list = keywords.split()

    news_list = []
    for word in word_list:
        if minimum_date is None:
            ans = News.objects.filter(title__contains=word)
        else:
            ans = News.objects.filter(title__contains=word,pub_date__gte=minimum_date)
        news_list = list(set(news_list) | set(ans))
    return render(request, 'politicians/news.html', context_for_news_list(request,news_list))

def context_for_news_list(request,news_list):
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

    news_upvoted_id = request.POST.get('upvoted',None)
    try:
        news_upvoted = News.objects.get(id=news_upvoted_id)
        user.upvote_news(news_upvoted)
    except:
        pass

    news_downvoted_id = request.POST.get('downvoted',None)
    try:
        news_downvoted = News.objects.get(id=news_downvoted_id)
        user.downvote_news(news_downvoted)
    except:
        pass

    news_undo_upvoted_id = request.POST.get('undo_upvoted',None)
    try:
        news_undo_upvoted = News.objects.get(id=news_undo_upvoted_id)
        user.undo_upvote_news(news_undo_upvoted)
    except:
        pass

    news_undo_downvoted_id = request.POST.get('undo_downvoted',None)
    try:
        news_undo_downvoted = News.objects.get(id=news_undo_downvoted_id)
        user.undo_downvote_news(news_undo_downvoted)
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

    news_rating = []
    for news in news_list:
        news_rating.append(news.get_news_rating())

    news_vote_status = []
    for news in news_list:
        if user_logged_in:
            news_vote_status.append(news.get_user_vote(user))
        else:
            news_vote_status.append(None)

    news_politician_set = []
    for news in news_list:
        news_politician_set.append(news.get_all_politicians())
        
    num_news_list = range(len(news_list))
    news_entry = zip(news_list,news_like_count,news_like_status,
                    news_rating,news_vote_status,news_politician_set,num_news_list)

    return {'news_heading': 'Notícias Recentes', 'news_entry': news_entry}


def news(request):
    news_list = News.objects.all().order_by('-pub_date')[:5]
    return render(request, 'politicians/news.html', context_for_news_list(request,news_list))

def all_news(request):
    news_list = News.objects.all().order_by('-pub_date')
    return render(request, 'politicians/news.html', context_for_news_list(request,news_list))

def login(request):
    return render(request, 'politicians/login.html')

def login_user(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            user = User.objects.get(username=name)
        except:
            context = {'message': "Usuario inexistente"}
            return render(request, 'politicians/login.html', context)
        if user.password == request.POST['password']:
            request.session['username'] = user.username
            return render(request, 'politicians/home.html')
        else:
            context = {'message': "Senha incorreta"}
            return render(request, 'politicians/login.html', context)
    else:
        return render(request, 'politicians/home.html')

def signup_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            try:
                User.objects.get(username=name)
                return render(request, 'politicians/login.html')
            except User.DoesNotExist:
                try:
                    user = User.objects.create(username=name, password=password1)
                    request.session['username'] = user.username
                    return render(request, 'politicians/home.html')
                except:
                    return render(request, 'politicians/login.html')
        else:
            return render(request, 'politicians/login.html')
    return render(request, 'politicians/home.html')

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

def favorites(request):
    try:
        username = request.session['username']
        user = User.objects.get(username__exact=username)
    except KeyError, User.DoesNotExist:
        return render(request, 'politicians/home.html')

    politicians_list = user.favorited_politicians()
    context = {'politicians_list': politicians_list}
    return render(request, 'politicians/favorites.html', context)

def favorite_politician(request):
    politician_id = request.POST['politician_id']
    original_page = request.POST['original_page']
    try:
        username = request.session['username']
        user = User.objects.get(username__exact=username)
        user.favorite_politician(politician_id)
    except KeyError, User.DoesNotExist:
        pass
    return redirect(original_page)

def unfavorite_politician(request):
    politician_id = request.POST['politician_id']
    original_page = request.POST['original_page']
    try:
        username = request.session['username']
        user = User.objects.get(username__exact=username)
        user.unfavorite_politician(politician_id)
    except KeyError, User.DoesNotExist:
        pass
    return redirect(original_page)
def call_crawler(request):
    news_added = add_news_to_db()
    return HttpResponse("{} news were added to DB".format(news_added))

def news_page(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    like_status = None
    vote_status = None
    try:
        username = request.session['username']
        user = User.objects.get(username__exact=username)
        user_logged_in = True
    except KeyError, User.DoesNotExist:
        user_logged_in = False
    rating = news.get_news_rating
    likes_count = news.get_likes_count
    try:
        like_status = news.does_user_like_me(user)
        vote_status = news.get_user_vote(user)
    except:
        pass

    polit_set = news.get_all_politicians()

    context = {'news': news, 'likes_count': likes_count, 'like_status': like_status, 'rating': rating, 'vote_status': vote_status,
        'polit_set': polit_set}
    return render(request, 'politicians/news_page.html', context)

def politica_comentario(request):
    return render(request, 'politicians/politica_comentario.html')
