from django.contrib import admin
from django.urls import path, include
from . import views

# from .decorators import check_recaptcha

urlpatterns = [
    path('', views.start, name='start'),
    path('home/', views.index, name='home'),
    path('news/', views.news, name='news'),
    path('account/', views.account, name='account'),

    path('journals/', views.journals, name='journals'),
    path('library/', views.library, name='library'),

    path('questions/', views.questions, name='questions'),
    path('information/', views.information, name='information'),
]
