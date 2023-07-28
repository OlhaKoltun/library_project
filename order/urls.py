from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.order_list_view, name='index_order'),
    path('<int:id>', views.order_detail_view, name='detail_order'),
    path('close/<int:id>/', views.order_close_view, name='close_order'),
    path('create/', views.order_create_view, name='create_order'),
]