from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import *



urlpatterns = [
    path('', main, name='posts_list_url'),
    path('news/', news, name="news_url"),
    path('wateroff/<int:id>/', woff_single, name='woff_single_url'),
    path('<str:slug>/', post_single, name='post_single_url')

]
