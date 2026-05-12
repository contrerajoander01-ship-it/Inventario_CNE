from django.urls import path
from . import views

urlpatterns = [
    path('', views.Equipment, name='Equipment'),
]