from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from main.models import News


class ArticleSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return News.objects.all().order_by('published')

    def lastmod(self, obj):
        return obj.date

    def location(self, obj):
        return obj.slug


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['index']

    def location(self, item):
        return reverse(item)
