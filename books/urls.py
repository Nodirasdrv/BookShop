from django.urls import path
from . import views


urlpatterns = [
    path('', views.CreateBookAPIView.as_view()),
    path('list/', views.ListBookAPIView.as_view()),
    path('update/<int:pk>/', views.UpdateBookAPIView.as_view()),
    path('detail/<int:pk>/', views.DeleteDetailBookAPIView.as_view()),
]