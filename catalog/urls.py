
from django.contrib import admin
from django.urls import path
from . import views, dbviews, author_views

urlpatterns = [
    path('index/', views.index),
    path('list/', views.list_books),  # URL, function
    path('country/', views.country_info),  # URL, function
    path('add_book/', dbviews.add_book),  # URL, function
    path('list_books/', dbviews.list_books),  # URL, function
    path('authors_list/', author_views.authors_list),  # URL, function
    path('authors_add/', author_views.authors_add),  # URL, function
    path('authors_edit/<int:id>', author_views.authors_edit),  # URL, function
    path('authors_delete/<int:id>', author_views.authors_delete),  # URL, function
    path('authors_home/', author_views.authors_home),  # URL, function
]
