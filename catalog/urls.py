
from django.contrib import admin
from django.urls import path
from . import views, dbviews

urlpatterns = [
    path('index/', views.index),
    path('list/', views.list_books),  # URL, function
    path('country/', views.country_info),  # URL, function
    path('add_book/', dbviews.add_book),  # URL, function
    path('list_books/', dbviews.list_books),  # URL, function
]
