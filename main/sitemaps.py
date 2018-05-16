from django.contrib.sitemaps import Sitemap

from main.models import News


class ArticleSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return News.objects.all().order_by('published')

    def lastmod(self, obj):
        return obj.published


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'
