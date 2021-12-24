from django.urls import path
from newsApp import views

urlpatterns = [
    path('index/', views.index),
    path('movies/', views.moviesinfo),
    path('sports/', views.sportsinfo),
    path('politics/', views.politicsinfo),
]
