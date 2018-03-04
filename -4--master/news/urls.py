from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', views.article, name='article'),
    url(r'$' , views.news, name='news'),

    ]

