from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Author
from .forms import AuthorForm


def authors_list(request):
    return render(request, 'authors_list.html',
                  {'authors': Author.objects.all()})


def authors_add(request):
    if request.method == "GET":
        form = AuthorForm()
        return render(request, 'authors_add.html',
                      {'form': form})
    else:
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()  # insert into table
            return redirect('/catalog/authors_list')
        else:
            return render(request, 'authors_add.html',
                          {'form': form})


def authors_edit(request, id):
    if request.method == "GET":
        author = Author.objects.get(id=id)
        form = AuthorForm(instance=author)
        return render(request, 'authors_edit.html',
                      {'form': form})
    else:
        author = Author.objects.get(id=id)
        form = AuthorForm(instance=author, data=request.POST)
        if form.is_valid():
            form.save()  # Update table
            return redirect('/catalog/authors_list')
        else:
            return render(request, 'authors_edit.html',
                          {'form': form})


def authors_delete(request, id):
     author = Author.objects.get(id=id)
     author.delete()
     return redirect('/catalog/authors_list')


def authors_home(request):
     authorscount = len(Author.objects.all())
     return render(request, 'authors_home.html',
                   {'authorscount' : authorscount})


def authors_name(request, id):
    try:
        author = Author.objects.get(id=id)
        return HttpResponse(author.fullname)
    except:
        return HttpResponse("Author Not Found!")