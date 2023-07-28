from django.shortcuts import render

from .models import Book
from author.models import Author


# def book_list_view(request):
#     context = {'books': Book.objects.all()}
#     return render(request, 'home.html', context)


def book_create_view(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        count = request.POST.get('count')

        book_object = Book.objects.create(name=name, description=description, count=count)
        context['object'] = book_object
        context['created'] = True

    return render(request, 'create_book.html', context=context)


def book_detail_view(request, id=None):
    book_object = None

    if id:
        book_object = Book.objects.get(pk=id)
    context = {'book': book_object}

    return render(request, 'book_detail.html', context=context)


def add_authors_to_book_view(request, id=None):
    book_object = None

    if id:
        book_object = Book.objects.get(pk=id)
    context = {'book': book_object}

    return render(request, 'book_detail.html', context=context)

