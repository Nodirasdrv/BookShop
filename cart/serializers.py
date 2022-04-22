from rest_framework import serializers

from books.models import Book
from .models import Basket


class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = '__all__'
        read_only_fields = ('customer', 'total_price')
        extra_kwargs = {
            'total_quantity': {'required': True}
        }

    def create(self, validated_data):
        total_quantity = validated_data.get('total_quantity')
        product = Book.objects.get(id=validated_data.get('product').id)
        total_price = product.price * total_quantity
        basket = Basket.objects.create(**validated_data, total_price=total_price)
        return basket


