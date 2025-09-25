from django.urls import path
from . import views

app_name = 'animals'

urlpatterns = [
    path('', views.home, name='home'),
    path('animals/', views.get_animals, name='get_animals'),
    path('animals/wild/', views.get_wild_animals, name='get_wild_animals'),
]