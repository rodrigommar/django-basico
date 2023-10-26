from django.urls import path
from blog import views

# blog/
urlpatterns = [
    path('', views.blog),
    path('exemplo/', views.exemplo),
]