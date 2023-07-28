from django.shortcuts import render

from .models import Order
from authentication.models import CustomUser


def order_list_view(request):
    context = {'orders': Order.objects.all()}
    print(context)

    return render(request, 'order_list.html', context)


def order_create_view(request):
    context = {}

    if request.method == 'POST':
        user = CustomUser.POST.get('user')
        book = request.POST.get('book')
        plated_end_at = request.POST.get('plated_end_at')
        order_object = Order.objects.create(user=user, book=book, plated_end_at=plated_end_at)
        context['object'] = order_object
        context['created'] = True

    return render(request, 'create_order.html', context=context)


def order_detail_view(request, id=None):
    order_object = None

    if id:
        order_object = Order.objects.get(pk=id)
    context = {'order': order_object}

    return render(request, 'order_detail.html', context=context)


def order_close_view(request, id=None):
    context = {}
    if id:
        try:
            order_object = Order.objects.get(pk=id)

            if order_object.end_at:
                order_object.delete()
                context['description'] = "The order was closed successful"
            else:
                context['description'] = f"The order can't be deleted, " \
                                         f"the user didn't return book yet"
        except Order.DoesNotExist:
            context['description'] = "The order doesn't exists in database"

    return render(request, 'close_order.html', context=context)
