from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ('account_user', )
        # extra_kwargs = {
        #     'image': {"required": True},
        #     'category': {"required": True},
        # }