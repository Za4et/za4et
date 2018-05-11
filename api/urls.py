from django.urls import path

app_name = 'api'
from . import views

urlpatterns = [
    path('get_news/<institute>/', views.get_news, name='get_news'),
    path('get_journals/<institute>/<form_edu>/<course>/', views.get_journals, name='get_journals')

]
