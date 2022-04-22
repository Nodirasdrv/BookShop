from django.urls import path
from. import views


urlpatterns = [
    path('', views.BasketListCreateAPIView.as_view()),
    path('detail/<int:pk>/', views.BasketDetailUpdateDelete.as_view()),
]