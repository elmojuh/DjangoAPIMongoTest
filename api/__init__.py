from django.urls import path
import os
from django.core.wsgi import get_wsgi_application
from django.http import JsonResponse
from pymongo import MongoClient

def get_db():
    client = MongoClient(
        host='test_mongodb',
        port=27017,
        username='root',
        password='pass',
        authSource="admin"
    )
    return client["animal_db"]

def home(request):
    return JsonResponse({"welcome": "Welcome to the world of Mongo!"})

def get_animals(request):
    db = None
    try:
        db = get_db()
        animals_cursor = db.animal_tb.find()
        animals = [
            {"id": animal["id"], "name": animal["name"], "type": animal["type"]}
            for animal in animals_cursor
        ]
        return JsonResponse({"animals": animals})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
def get_wild_animals(request):
    db = None
    try:
        db = get_db()
        wild_cursor = db.animal_tb.find({"type": "Wild"})
        animals = [
            {"id": animal["id"], "name": animal["name"], "type": animal["type"]}
            for animal in wild_cursor
        ]
        return JsonResponse({"animals": animals})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
    
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

application = get_wsgi_application()
urlpatterns = [
    path('', home, name='home'),
    path('animals/', get_animals, name='get_animals'),
]