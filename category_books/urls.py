from django.urls import path

from category_books import views

urlpatterns = [
    path('', views.CreateCategory.as_view()),
]