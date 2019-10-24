from django.db import models

# Create your models here.

class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price


