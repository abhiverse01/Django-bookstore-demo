# books/urls.py

from django.urls import path
from .views import BookListCreate

urlpatterns = [
    path('api/books/', BookListCreate.as_view(), name='book-list-create'),
]