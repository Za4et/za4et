from django.contrib import admin
from django.urls import path, include
from . import views

# from .decorators import check_recaptcha

urlpatterns = [
    path('', views.start, name='start'),
    path('home/', views.index, name='home'),
    path('journals/', views.journals, name='journals'),
    path('library/', views.library, name='library'),
    path('feedback/', views.feedback, name='feedback'),
    path('information/', views.information, name='information'),
]
