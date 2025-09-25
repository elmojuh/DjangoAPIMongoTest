from django.urls import path, include

urlpatterns = [
    path('', include('animals.urls')),
]