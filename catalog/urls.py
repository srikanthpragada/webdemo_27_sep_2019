
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('list/', views.list_books),  # URL, function
    path('country/', views.country_info),  # URL, function
]
