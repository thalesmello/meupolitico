from django.conf.urls import patterns, url

from politicians import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)