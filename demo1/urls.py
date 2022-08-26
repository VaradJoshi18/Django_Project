from django.contrib import admin
from django.urls import path
# from medic_kit.views import hello
from . import views

urlpatterns = [
    path('/', views.helloPage),
    
]