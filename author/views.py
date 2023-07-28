from django.shortcuts import render

from .models import Author


def author_list_view(request):
    context = {'authors': Author.objects.all()}

    return render(request, 'authors_list.html', context)


def author_create_view(request):
    context = {}

    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        patronymic = request.POST.get('patronymic')
        author_object = Author.objects.create(name=name, surname=surname, patronymic=patronymic)
        context['object'] = author_object
        context['created'] = True

    return render(request, 'create_author.html', context=context)


def author_detail_view(request, id=None):
    author_object = None

    if id:
        author_object = Author.objects.get(pk=id)
    context = {'author': author_object}

    return render(request, 'author_detail.html', context=context)


def author_delete_view(request, id=None):
    context = {}
    if id:
        try:
            author_object = Author.objects.get(pk=id)
            books_count = author_object.books.all().count()

            if books_count == 0:
                author_object.delete()
                context['description'] = "The author was deleted successful"
            else:
                context['description'] = f"The author can't be deleted, " \
                                         f"he has {books_count} books attached"
        except Author.DoesNotExist:
            context['description'] = "The author doesn't exists in database"

    return render(request, 'delete_author.html', context=context)



