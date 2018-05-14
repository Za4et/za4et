from django.conf.urls import url
from django.contrib.auth.views import logout
from django.urls import path
from main.decorators import check_recaptcha
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('home/', views.index, name='home'),
    path('news/', views.news, name='news'),
    path('tag/<tag_name>/', views.tag, name='tag'),
    url(r'news/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', views.article, name='article'),
    path('account/', views.account, name='account'),
    path('login/', check_recaptcha(views.logn), name='login'),
    path('logout/', logout),
    path('journals/', views.journals, name='journals'),
    path('library/', views.library, name='library'),
    path('questions/', views.questions, name='questions'),
    path('information/', views.information, name='information'),
    path('zip/', views.get_files, name='jgroup'),
    path('search/', views.res_search, name='res_search')
]
