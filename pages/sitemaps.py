from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Proje


class PagesSitemap(Sitemap):

    def items(self):
        return ['index', 'about', 'contact', 'proje', 'vizyon',]

    def location(self, item):
        return reverse(item)


class ProjeSitemap(Sitemap):

    def items(self):
        return Proje.objects.all()