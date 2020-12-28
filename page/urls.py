from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import *



urlpatterns = [
    path('<str:slug>/', page_single, name='page_single_url'),

]
