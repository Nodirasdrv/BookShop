from django.db import models


class Category(models.Model):
    genre = models.CharField(max_length=200)
    new_release = models.DateField()
    best_seller = models.CharField(max_length=200)

    def __str__(self):
        return self.genre
