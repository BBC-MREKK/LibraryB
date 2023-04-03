from django.urls import path
from .views import book_list, book_detail

urlpatterns = [
    path('home/', book_list, name='book_list'),
    path('<int:pk>/', book_detail, name='book_detail'),
]