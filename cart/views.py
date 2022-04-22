from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Basket
from .serializers import BasketSerializer


class BasketListCreateAPIView(generics.ListCreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

    def perform_create(self, serializer):
        return serializer.save(customer=self.request.user)


class BasketDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = [IsAuthenticated]




