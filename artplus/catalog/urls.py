from django.urls import path

from .views import *

urlpatterns = [
    path('',main),
    path('about_us',about_us),
    path('catalog',catalog),
    path('feedback',feedback),
    path('contacts',contacts),
    path('square',square),
    path('figur',figur),
    path('besser',besser),
    path('borts',borts)
]