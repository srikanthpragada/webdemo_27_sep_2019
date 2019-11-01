import requests
from django.http import HttpResponse
from django.shortcuts import render

from .models import Book

# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome To Catalog Application</h1>")


def list_books(request):
    books = [
        Book("Java Complete Reference", "Herbert", 500),
        Book("Python Tricks", "Dan Bader", 250),
        Book("Oracle Database SQL", "Jason Price", 450)
    ]

    # render(requests, template, context)
    return render(request, 'list_books.html', {'books': books})


def country_info(request):
    if 'code' in request.GET:
        code = request.GET['code']  # country code
        resp = requests.get(f"https://restcountries.eu/rest/v2/alpha/{code}")
        if resp.status_code == 200:
            details = resp.json()
            return render(request, 'country_info.html', {'code': code, 'details': details})
        else:
            return render(request, 'country_info.html', {'code': code, 'error': 'Sorry! Invalid country code!'})

    return render(request, 'country_info.html')

def ajax_demo(request):
    return render(request,'ajax_demo.html')