from django.conf.urls import patterns, url

from politicians import views

urlpatterns = patterns('',
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /index
    url(r'^index/$', views.index, name='index'),
    # ex: /politicians/
    url(r'^politicians/$', views.politicians, name='politicians'),
    # ex: /politicians/1/
    url(r'^politicians/(?P<politician_id>\d+)/$', views.politician_profile, name='politician_profile'),
    # ex: /news/
    url(r'^news/$', views.news, name='news'),
    # ex: /news/all/
    url(r'^news/all/$', views.all_news, name='all_news'),
)