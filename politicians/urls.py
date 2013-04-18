from django.conf.urls import patterns, url

from politicians import views

urlpatterns = patterns('',
    # ex: /
    url(r'^$', views.home, name='home'),
    # ex: /home/
    url(r'^home/$', views.home, name='home'),
    # ex: /index
    url(r'^index/$', views.home, name='index'),
    # ex: /politicians/
    url(r'^politicians/$', views.politicians, name='politicians'),
    # ex: /politicians/1/
    url(r'^politicians/(?P<politician_id>\d+)/$', views.politician_profile, name='politician_profile'),
    # ex: /login/
    url(r'^login/$', views.login, name='login'),
    # ex: /login_user/
    url(r'^login_user/$', views.login_user, name='login_user'),
    # ex: /logout/
    url(r'^logout/$', views.logout, name='logout'),
    # ex: /news/
    url(r'^news/$', views.news, name='news'),
    # ex: /news/all/
    url(r'^news/all/$', views.all_news, name='all_news'),
    # ex: /search/
    url(r'^search/$', views.search, name='search'),
    # ex: /search_results/
    url(r'^search_results/$', views.search_results, name='search_results'),
)