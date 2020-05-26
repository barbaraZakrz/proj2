from django.urls import path
from . import views

urlpatterns = [
    path('', views.nauczyciel_list, name='nauczyciel_list'),
]