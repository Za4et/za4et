from django.db import models

# Create your models here.
from django.urls import reverse
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=300)
    slug = AutoSlugField(populate_from='title')



    def __str__(self):
        return self.title


class News(models.Model):
    class Meta:
        verbose_name='Новости'
        ordering = ['-published']
    title = models.CharField(max_length=500,blank=True, null=True)
    text = RichTextField()
    file = models.FileField(verbose_name='Прикрепить документ',blank=True, null=True, upload_to='news/')
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)
    slug = AutoSlugField(populate_from='title')
    def __str__(self):
        return  str(self.title)
    def get_absolute_url(self):
        year = str(self.published.year)
        month  = str(self.published.strftime('%m'))
        day = str(self.published.strftime('%d'))
        slug = str(self.slug)
        returned = '/news'+'/'+year+'/'+month+'/'+day +'/' +slug+'/'
        return returned




