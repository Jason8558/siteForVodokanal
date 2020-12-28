from django.shortcuts import render
from .models import *
from blog.models import Menuitem

def page_single(request, slug):
    page = Page.objects.get(slug__iexact=slug)
    menu = Menuitem.objects.all()
    return render(request, 'page/page.html', context={'page':page, 'menu':menu})
