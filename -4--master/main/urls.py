from django.contrib import admin
from django.urls import path, include
from . import views
# from .decorators import check_recaptcha

urlpatterns = [
    path('' , views.index , name='home'),
]