from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect


def main(request):
    posts = Post.objects.filter().exclude(category=4)
    paginator = Paginator(posts, 6)
    postwoff = Wateroff.objects.all()
    woff_paginator = Paginator(postwoff, 3)
    pagewoff = woff_paginator.get_page(1)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    menu = Menuitem.objects.all()
    return render(request, 'blog/base.html', context={'pnhvs': pagewoff, 'posts': page, 'menu':menu})

def post_single(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    menu = Menuitem.objects.all()

    return render(request, 'blog/post_single.html', context={'post':post, 'menu':menu })

def woff_single(request, id):
    post = Wateroff.objects.get(id__exact=id)
    menu = Menuitem.objects.all()

    return render(request, 'blog/woff_single.html', context={'post':post, 'menu':menu })

def news(request):
    posts = Post.objects.all()
    menu = Menuitem.objects.all()
    paginator = Paginator(posts, 12)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    return render(request, 'blog/news.html', context={'posts':page, 'menu':menu })
