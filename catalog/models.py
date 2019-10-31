from django.db import models

# Create your models here.

class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price


class Author(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.fullname} - {self.email} - {self.mobile}"
