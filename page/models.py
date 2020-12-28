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
class Page(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = RichTextField()
    date_pub = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '{}'.format(self.title)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
            super().save(*args, **kwargs)
