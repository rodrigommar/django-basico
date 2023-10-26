from django.urls import path
from home import views

# home/
urlpatterns = [
    path('', views.home),   
]