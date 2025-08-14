from django.http import JsonResponse
from .mongo import get_db

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
    