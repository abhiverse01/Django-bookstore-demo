from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
# Create your views here.

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        external_data = fetch_external_data('https://api.example.com/data')
        # process external data as needed
        serializer.save()
        