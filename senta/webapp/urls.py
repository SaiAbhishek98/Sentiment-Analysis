from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name = 'index'), 
    path('tweet/', views.print_tweets, name = 'print_tweets'),
]
