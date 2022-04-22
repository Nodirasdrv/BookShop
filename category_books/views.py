from django.shortcuts import render
from rest_framework import response, generics
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.views import APIView

from .models import Category
from .serializers import CategorySerializer


class CreateCategory(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return response.Response(serializer.data)


