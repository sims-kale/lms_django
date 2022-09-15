from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('getBooks/', views.getData)
]
