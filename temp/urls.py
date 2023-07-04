from django.urls import path
from . import views


urlpatterns = [
    path('temp/', views.temp_here, name='temp_here'),
    path('temp/discover', views.temp_somewhere, name='temp_somewhere'),
]