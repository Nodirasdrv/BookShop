from django.db import models
from django.contrib.auth import get_user_model

from category_books.models import Category

User = get_user_model()


class Edition(models.Model):
    edition = models.CharField(max_length=200)


class Book(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    amount = models.IntegerField()
    image = models.ImageField(upload_to='books',
                              default='no_book.jpg', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)
    account_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    id_edition = models.ForeignKey(Edition, on_delete=models.SET_NULL, null=True,
                                 blank=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    biography = models.TextField()
    age = models.IntegerField()
    image = models.ImageField(upload_to='authors',
                              default='no_book.jpg')

    def __str__(self):
        return f"{self.name} {self.surname}"


class Book_Author(models.Model):
    id_book = models.ForeignKey(Book, on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)
    id_author = models.ForeignKey(Author, on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)

#
# class Cart(models.Model):
#     id_user = models.ForeignKey(User, on_delete=models.SET_NULL,
#                                  null=True,
#                                  blank=True)
#     id_book = models.ForeignKey(Book, on_delete=models.SET_NULL,
#                                  null=True,
#                                  blank=True)
#     total = models.IntegerField()




