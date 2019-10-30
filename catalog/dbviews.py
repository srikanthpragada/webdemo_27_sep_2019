from django.shortcuts import render
from .forms import BookForm
import sqlite3


def add_book(request):
    if request.method == 'GET':
        book_form = BookForm()
        return render(request, 'add_book.html', {'form': book_form})
    else:  # post
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            # add new book to Books table
            title = book_form.cleaned_data['title']
            author = book_form.cleaned_data['author']
            price = book_form.cleaned_data['price']
            try:
                con = sqlite3.connect(r"e:\classroom\python\sep27\library.db")
                cur = con.cursor()
                cur.execute("insert into books(title,author,price) values(?,?,?)",
                            (title, author, price))
                if cur.rowcount == 1:
                    con.commit()
                    book_form = BookForm()  # Empty form
                    return render(request, 'add_book.html',
                                  {'form': book_form,
                                   'message': 'Book has been added!'})
            except:
                return render(request, 'add_book.html',
                              {'form': book_form,
                               'message': 'Could not add book due to error!'})
            finally:
                con.close()

        else:
            return render(request, 'add_book.html', {'form': book_form})


def list_books(request):
    try:
        con = sqlite3.connect(r"e:\classroom\python\sep27\library.db")
        cur = con.cursor()
        cur.execute("select * from books order by id")
        books = cur.fetchall()
        con.close()
        return render(request, 'list_db_books.html', {'books': books})
    except:
        return render(request, 'list_db_books.html',
                      {'message': 'Sorry! Could not retrieve books!'})
