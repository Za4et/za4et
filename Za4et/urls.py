"""Za4et URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path, include

from Za4et import settings


def sitemap(request):
    return HttpResponse('Sitemap.xml')


def google_bot(request):
    return render(request, 'google6a6420e729ccc5fb.html')


def yandex_bot(request):
    return render(request, 'yandex_2b22988392c6cecf.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v0/', include('api.urls')),
    path('sitemap.xml/', sitemap),
    path('', include('main.urls')),
    path('google6a6420e729ccc5fb.html/', google_bot),
    path('yandex_2b22988392c6cecf.html/', yandex_bot)

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
