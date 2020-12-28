from django.db import models
from django.shortcuts import reverse
from time import time
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey
def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))
def set_slug():
    return gen_slug('post')

def get_first_category():
    return Category.objects.first().title

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, default=set_slug)
    body = RichTextUploadingField(max_length=3000)
    category = models.ManyToManyField('Category', blank=False, related_name='posts', default=get_first_category)
    date_pub = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    class Meta:
        ordering = ['-date_pub']
        verbose_name = 'новость'
        verbose_name_plural = 'Новости'

    # def save(self):
    #     if not self.id:
    #         self.slug = gen_slug(self.title)
    #         Post.save(force_update=True)

    def __str__(self):
        return self.title
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
            super().save(*args, **kwargs)



class Menuitem(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    url = models.CharField(unique=False, default='#', max_length=150)

    class Meta:
        ordering = ['lft']

    def __str__(self):
        return '{}'.format(self.name)

class Wateroff(models.Model):
    city = models.ForeignKey('Cities',on_delete=models.CASCADE, verbose_name=u"Населенный пункт",max_length=50)
    date_of_off = models.DateTimeField()
    date_of_on = models.DateTimeField()
    reason = models.CharField(max_length=50)
    adresses = models.TextField()

    class Meta:
        ordering = ['-id']
        verbose_name = 'отключение ХВС'
        verbose_name_plural = 'Отключения ХВС'


    def __str__(self):
        return '{}'.format(self.date_of_off.strftime("%d/%m/%Y %H:%M")) + ", " +'{}'.format(self.city)

class Cities(models.Model):
    title = models.CharField(verbose_name=u"Наименование", max_length=50)

    def __str__(self):
        return '{}'.format(self.title)
