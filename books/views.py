from django.shortcuts import render
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView

# from .paginators import CarsPagination
from .paginators import BookPagination
from .permissions import IsAuthorOrReadOnly
from .serializers import BookSerializer
from books.models import Book


class ListBookAPIView(ListAPIView):
    pagination_class = BookPagination
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny, ]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description']


class CreateBookAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        return serializer.save(account_user=self.request.user)


class UpdateBookAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthorOrReadOnly, ]


class DeleteDetailBookAPIView(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthorOrReadOnly, ]




